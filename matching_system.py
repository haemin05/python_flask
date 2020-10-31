# matching system
# 1.사용자가 원하는 멘토의 정보를 고른다 2.사용자가 원하는 정보와 가장 비슷한 멘토를 뽑는다. 만점은 10점.
# 최종 결과는 점수로 줄 것. 예) 성별이 다르면 10점에서 1점을 깎는다.

# 만약 사용자가 영어 철자를 틀려도 알아서 수정해주는 프로그램 생각해보기

mentor1 = ['boy', '23', 'math', 'science']
mentor2 = ['boy', '25', 'history', 'society']
mentor3 = ['girl', '21', 'english', 'art']
mentor4 = []
mentor5 = []
mentor6 = []
mentor7 = []
mentor8 = []
mentor9 = []
mentor10 = []

subject_of_interest = input('-Subject-\n[math] [science] [history] [society] [english] [art]\nSubject of interest = ')
preferred_age = int(input('Preferred age = '))
preferred_gender = input('-example-\n[boy] [girl]\nPreferred gender = ')

subject_list = subject_of_interest.split()

