from sys import exit
from random import randint
from textwrap import dedent

class views:
    def enter(self):
        print("아직 만들지 않은 장면입니다.")
        print("상속해 입장()을 구현하세요")
        exit(1)

class death(views):#death

    ddd=[
        "사망,사망 개못해",
        "어머니가 자랑스러하겠네^^",
        "패배자 쉨ㅋㅋ",
        "내가 기르는 강아지도 그것보다 잘하겠다",
        "하...걍 포기해"
    ]    

    def enter(self):
        print(death.ddd[randint(0, len(self.ddd)-1)])
        exit(1)
        
class middle_roun(views): #중악복도
        def enter(self):
            print(dedent("""
                페르칼 25번 행성의 고전족은 여러분의 우주선에 침략해서 모든
                승무원을 죽였습니다. 당신은 마지막 생존자이며 마지막 임무로
                무기고에서 중성자파괴탄을 가져와 함교에 설치하고 구명정에 
                타기 전에 우주선에 폭파해야 합니다.

                붉은 비늘 피부, 시커먼 떄가 낀 이빨, 증오로 가득 찬 몸에서
                흐르듯 이어지는 사악한 광대 복장의 고던인이 뛰쳐 나오는 동안
                당신은 중앙 복도에서 무기고로 내달리고 있었습니다. 고던인은
                무기고로 가는 문을 가로막고 당신을 날려버리려 무기를 겨누는
                참입니다

                1.발사
                2.회피
                3.반사
                """))
            doing=input("> ")

            if doing=="발사" or doing=="1":
                print(dedent("""
                1111111111111111111111111111111111111111111111111111111111
                당신은 광선총으 ㄹ뺴들기가 무섭게 고던인르 쏘아버립니다.
                고던인의 광대 옷이 휘날려 몸을 숨겨주고
                당신을 조준을 흩뜨립니다. 광선은 옷을 맞추었지만 고던인은 왖너히
                농쳐버립니다. 어머니가 사준 신상 옷을 모조리 빡쳐버리자 
                고던인은 광기 어린 분노에 빠져들어 당신을 죽을 떄까지
                얼굴을 쏘아댑니다. 고던인은 당신을 먹어치웁니다.
                """))
                return 'death'
            if doing=="회피" or doing=="2":
                print(dedent("""
                국제경기급 권투 선수처럼 달리고 피하고 구르고 오른쪽으로
                미끄러져 고던인의 광선총이 당신의 머리 옆을 빗겨 쏘도록
                합니다. 예술적인 횡피를 하던 와중 그만 발이 미끄러져 금속
                벽에 머리를 찍고 기절합니다.잠시 후 정치을 차리자만
                고던인은 그저 머리를 짓밟아 죽이고만 잡아 먹을 뿐입니다.
                """))
                return 'death'
            if doing=="반사" or doing=="3":
                print(dedent("""
                운좋게도 당신은 학교에서 고던어 욕설을 배웠습니다. 아는
                고던 농담을 하나 합니다
                ang gimochi
                고던인은 멈춰서서 웃지 않으려 애쓰지만, 결국 웃음보가
                터지자 꼼짝도 하지 못합니다. 당신은 고던인이 웃어대는
                틈에 뛰쳐나가 정통으로 머리를 맞춰 쓰러뜨리고 무기고의
                문으로 뛰어듭니다
                """))
                return 'r_army'

            
class r_army(views):#레ㅐ이저 무기고
        def enter(self):
            print(dedent("""
                당신은 무기로로 뛰어들어 구르고는 쪼그려 앉아 혹시
                숨어있을지도 모르는 고던인을 찾아 방을 쌀핍니다. 쥐 죽은
                듯이, 지나칠 만큼 조용합니다. 일어서서는 문 건너편으로
                달려 보관함에서 중성자파괴탄을 찾습니다. 보관함은
                비밀번호로 잠겨 있고 중성자파괴탄을 꺼내려는 비밀번호를
                알아내야만 합니다. 비밀번호를 10ㅎ번틀리면 자물쇠는 영원히 
                잠기고 폭탄을 꺼낼 수 없습니다. 비밀번호는 3자리
                수입니다. 
                """))
            rn=["0","0","0"]
            rn[0]=f"{randint(1,9)}"
            rn[1]=f"{randint(1,9)}"
            rn[2]=f"{randint(1,9)}"
            num=True
            while(num):
                if(rn[0]==rn[1]):
                    rn[1]=f"{randint(1,9)}"
                else:
                    if(rn[0]==rn[2] or rn[1]==rn[2]):
                        rn[2]=f"{randint(1,9)}"
                    else:
                        num=False
            rn1=rn[0]+rn[1]+rn[2]
            my_code= str(input("숫자 3자리를 입력하세요 : "))
            code_num=0
            s_cnt=0
            b_cnt=0
            while my_code != rn1:
                print("삐삐삐빅")
                code_num+=1
                for i in range(0, 3):
                    for j in range(0, 3):
                        if(my_code[i]== str(rn[j]) and i == j):
                            s_cnt += 1
                        elif(my_code[i] == str(rn[j]) and i != j):
                            b_cnt += 1
                print("결과 : [", s_cnt, "] Strike [", b_cnt, "] Ball")
                s_cnt=0
                b_cnt=0
                my_code= str(input("숫자 3자리를 입력하세요 : "))      
                if my_code == rn1:
                    print(dedent("""
                        보관함이 철컥하며 열리며 밀폐가 풀리자 공기가
                        새어나옵니다. 중서자파괴탄을 움켜쥐고 설치해야 할 장소인
                        함교를 항해 할 수 있는 한 가장 빠른 속도로 내달립니다.
                    """))
                    return "gkry"
                    
                elif code_num==10:
                    print(dedent("""
                        마지막 기회가 지나자 자물쇠가 웅웅거리며 기계장치가 엉겨 
                        붙으며 녹아내리는 소름끼치는 소리가 들립니다.
                        당신은 거기 주저앉아 있기를 마음먹었고, 결국 고던 우주선이
                        당신에 우주선을 터뜨려 죽음을 맞습니다.
                    """))
                    return "death"

            
class gkry(views):#함교
    def enter(self):
        print(dedent("""
            겨드랑이에 중서장파괴탄을 끼고 함교로 뛰어들어어
            조종권을 탈취하던 고던인 5명을 놀래킵니다. 그 모두가
            아까 본 고던인보다도 더 흉축한 광대 복장을 하고
            있습니다. 고던인들은 아직 무기를 뽑지는 않았는데,
            활성화된 폭탄을 든 걸 보자 더욱 더 터뜨리지 않고
            싶어합니다.
                
            1.폭탄 던지기
            2.천천히 폭탄 설치하기
            """))
        doing=input("> ")

        if doing=="폭탄던지기"or doing=="1":
            print(dedent("""
            당신은 당황해서 고던인 무리에 폭탄을 집어 던지고는
            문으로 펄쩍 뒤어 오릅니다. 폭탄을 놓자마자 고던인
            하나가 등 뒤를 정확히 쏴 맞춰 죽여버립니다.
            당신은 죽어가는 동안 다른 고던인이 미친 듯이 폭찬을
            해체하려 달려드는 것을 봅니다. 죽음을 맞는 동안
            폭탄이 터지며 고던인 모두가 터져 나가리라고
            생각합니다
            """))
            return 'death'

        elif doing=="천천히 폭탄 설치하기" or doing=="2":
            print(dedent("""
            폭탄을 광선총으로 겨누자 고던인들은 두 손을 들고
            삐질삐질 땀을 흘리기 시작합니다. 당신은 문뒤에
            바짝 붙어서는, 문을 열고, 광선총을 그대로 겨눈 채로,
            조심스레 폭탄을 바닥에 설치합니다. 곧 이어 문밖으로
            뛰쳐나가 닫기 단추를 두들기고는 잠금장치를 쏴 갈겨
            고던인들이 빠져 나올 수 없도록 만들어버립니다.
            이제 폭탄을 설치되었고, 이 깡통에서 벗어나도록
            구명정으로 내달립니다.
            """))
            return 'rnaudwjd'
        else:
            print("처리할 수 없습니다")
            return "gkry"

class rnaudwjd(views):#구명정
        def enter(self):
            print(dedent("""
                우주선이 통쨰로 폭발하기 전에 구명정에 닿기 위해
                우주선을 가로질러 필사적으로 달립니다. 우주선에는
                고던인이 거의 없어 방해받지 않고 질주합니다. 구명정이
                있던 방에 도달한 당신은 어떤 걸 탈지 하나를 골라야
                합니다. 이 가운데 몇개는 손상되었 수도 있지만 살펴볼 시간이 없습니다.
                구명정은 5대가 있습니다. 몇번을 타겠습니까?
                """))
            ok_rnaudwjd=randint(1,5)
            print(ok_rnaudwjd)
            my_code=input("[구명정번호] ")
            print(ok_rnaudwjd)

            if (int(my_code)) != ok_rnaudwjd:
                print(dedent(f"""
                {my_code}번 구명정으로 뛰어들어 탈출 단추를 누릅니다.
                구명정이 우주의 진공으로 나아가지마자, 선채로
                파멸해 찌그러져 들며 당신을 곤약처럼 으스러뜨립니다.
                """))
                return 'death'
            else:
                print(dedent(f"""
                    {my_code}번 구명정으로 뛰어들어 탈출 단추를 누릅니다.
                    구명정은 가볍게 우주로 미끄러져 나가며 아래의 행성으로 향합니다. 
                    행성으로 향하는 동안 뒤를 돌아보자 당신에 우주선이 붕괴했다가는 
                    밟은 별처럼 폭발하며 고던 우주선까지 휩쓸어 버리는 것을 확인합니다.))
                    """))
                return 'gold'
class gold(views):
    def enter(self):
        print(dedent("""
                구명정 뒤에는 엄청나게 많은 돈들이 있었습니다.
                하지만 이런 그 사이에 작은 고던인이 한명 자고있네요
                고던인은 일어나 게임을 하자고 하네요.
                """))
        rn=int(f"{randint(1,100)}")
        print(rn)
        num=1
        num_try=0
        print("1~100 숫자 업다운 시작 ?회 이상 탈락")
        print("-------------------------")
        while(rn != num):
            num = int(input("1 ~ 100 사이의 숫자를 입력하세요 : "))
            if (num > rn):
                print("Down")
            elif (num < rn):
                print("Up")
            num_try += 1
        if(num_try<8):
            print(f"{num_try}회 통과다")
            return 'end'
        else:
            print(f"{num_try}회 음....안되겠다")
            return 'death'
        
class end(views):
    def enter(self):
        print("승리했습니다! 잘했어여")
        return 'end'

class wleh(views):#지도
    viewss={
        'middle_roun':middle_roun(),
        'r_army':r_army(),
        'gkry':gkry(),
        'rnaudwjd':rnaudwjd(),
        'death':death(),
        'gold':gold(),
        'end':end()
    }
    def __init__(self, start_scene):
        self.start_scene = start_scene

    def opening_scene(self):
        return self.next_scene(self.start_scene)

    def next_scene(self, scene_name):
        val = wleh.viewss.get(scene_name)
        return val

class eg(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter()


game_map=wleh('middle_roun')
egs=eg(game_map)
egs.play()


