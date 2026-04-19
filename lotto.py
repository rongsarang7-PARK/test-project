import random

def generate_lotto_numbers():
    # 1부터 45까지의 숫자 중 6개를 무작위로 선택합니다.
    lotto_numbers = random.sample(range(1, 46), 6)
    lotto_numbers.sort()  # 보기 좋게 정렬합니다.
    return lotto_numbers

if __name__ == "__main__":
    print("✨ 이번 주 추천 로또 번호입니다! ✨")
    print(generate_lotto_numbers())
