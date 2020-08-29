import torch
import os
import torch.nn as nn
import time
import shutil
from datetime import datetime
import torch.optim as optim
from tqdm import tqdm
import torchvision.models as models
from tensorboard_logger import configure, log_value
from utils.compute_average import  AverageMeter

class H_MODEL(object):
    def __init__(self, args, train_loader, test_loader):

        self.test_loader = test_loader
        self.train_loader = train_loader
        self.criterion = nn.CrossEntropyLoss().cuda()
        self.lr = args.lr
        self.model_name = "nk"
        self.epochs = args.epochs
        self.gamma = args.gamma
        self.best_val_acc = 0
        self.num_train = len(self.train_loader.dataset)
        self.use_tesorboard = args.use_tensorboard
        self.batch_size = args.batch_size
        self.logs_dir = args.logs_dir
        now = datetime.now()
        self.time = now.strftime("%H:%M:%S")
        self.save_dir = './' + args.save_dir
        if not os.path.exists(self.save_dir):
            os.mkdir(self.save_dir)

        if self.use_tesorboard:
            tensorboard_dir = self.logs_dir + args.model_name
            print('[*] Saving tensorboard logs to {}'.format(tensorboard_dir))
            if not os.path.exists(tensorboard_dir):
                os.makedirs(tensorboard_dir)
            configure(tensorboard_dir)

        if args.model_name == 'vgg16':
            self.model = models.resnet18()
            self.model.fc = nn.Linear(512, 6)

            print(self.model)

            self.optimizer = torch.optim.SGD(filter(lambda p: p.requires_grad,
                                                    self.model.parameters()),
                                             lr=self.lr,
                                             momentum=args.momenyum,
                                             weight_decay=args.weight_decay)

            self.scheduler = optim.lr_scheduler.StepLR(self.optimizer, step_size=60,
                                                       gamma=self.gamma, last_epoch=-1)

            num_params = sum(p.numel() for p in self.model.parameters()
                             if p.requires_grad)
            print('The number of parametrs of models is', num_params)

            if args.save_load:
                location = args.save_location
                print("locaton", location)
                checkpoint = torch.load(location)
                self.model.load_state_dict(checkpoint['state_dict'])

    def train(self):

        self.model.train()

        for epoch in range(self.epochs):
            print('\nEpoch: {}/{} - LR: {:.6f}'.format(epoch + 1, self.epochs,
                                                           self.optimizer.param_groups[0]
                                                           ['lr'], ))

            train_losses, train_accs = self.train_one_epoch(epoch)
            self.scheduler.step(epoch)

    def train_one_epoch(self, epoch):
        losses = AverageMeter()
        top1 = AverageMeter()
        batch_time = AverageMeter()
        tic = time.time()

        with tqdm(total=self.num_train) as pbar:
            for i, (inputs, targets, _) in enumerate(self.train_loader):
                inputs, targets = inputs.cuda(), targets.cuda()
                output = self.model(inputs)
                loss = self.criterion(output, targets)
                self.optimizer.zero_grad()
                loss.backward()
                self.optimizer.step()

                prec1 = self.accuracy(output.data, targets)[0]
                losses.updata(loss.item(), inputs.size()[0])
                top1.update(prec1.item(), inputs.size()[0])

                toc = time.time()
                batch_time.update(toc - tic)

                pbar.set_description(
                (
                         "{:.1f}s - model1_loss: {:.3f} - model1_acc: {:.3f}".format(
                            (toc - tic), losses.avg, top1.avg
                            )
                        )
                )

                pbar.update(self.batch_size)

                if self.use_tensorboard:
                    iteration = epoch * len(self.train_loader) + 1

                    log_value('train_loss_%d' % (i + 1), losses.avg, iteration)
                    log_value('train_acc_%d' % (i + 1), top1.avg, iteration)

            return losses, top1

    def test(self):
        path = "/tmp/pycharm_project_exam_vision/save/best_1.pth.tar"

        self.load_model(path)
        self.model.eval()
        temp = []
        for i, (inputs, targets, _) in enumerate(self.test_loader):
            inputs = inputs.cuda()
            outputs = self.model(inputs)
            _, predicted = torch.max(outputs.data, 1)
            predicted = predicted.cpu()
            predicted = predicted.numpy()[0]
            temp.append(predicted)

        return temp

    def accuracy(self, output, target, topk=(1,)):
        maxk = max(topk)
        batch_size = target.size(0)
        _, pred = output.topk(maxk, 1, True, True)
        pred = pred.t()
        correct = pred.eq(target.view(1, -1).expand_as(pred))

        res = []
        for k in topk:
            correct_k = correct[:k].view(-1).float().sum(0)
            res.append(correct_k.mul_(100.0 / batch_size))
        return res

    def save_checkpoint(self, i, state, is_best):

        filename = self.model_name + "_" + self.time + "_" + str(i + 1) + '_ckpt.pth.tar'
        ckpt_path = os.path.join(self.save_dir, filename)
        torch.save(state, ckpt_path)

        if is_best:
            filename = self.model_name + "_" + self.time + "_" + str(i + 1) + '_model_best.pth.tar'
            shutil.copyfile(
                ckpt_path, os.path.join(self.save_dir, filename)
            )

    def load_model(self, path):

        checkpoint = torch.load(path)
        self.model.load_state_dict(checkpoint['model_state'])