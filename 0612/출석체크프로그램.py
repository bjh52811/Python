class AttendanceManager:
    def __init__(self):
        self.attendance_book = {}

    def add_student(self, name):
        """새로운 학생을 출석부에 등록합니다."""
        if name in self.attendance_book:
            print(f"⚠️ 이미 등록된 학생입니다: {name}\n")
        else:
            self.attendance_book[name] = {"상태": "미확인", "점수": 0}
            print(f"✅ {name} 학생이 등록되었습니다.\n")

    def mark_attendance(self, name, attendance_type, late_hours=0):
        """출석 유형과 지각 시간에 따라 상태와 점수를 업데이트합니다."""
        if name not in self.attendance_book:
            print(f"⚠️ 등록되지 않은 학생입니다: {name}\n")
            return

        if attendance_type == '1':
            self.attendance_book[name] = {"상태": "정상 출석", "점수": 3}
            
        elif attendance_type == '2':
            if late_hours == 1:
                self.attendance_book[name] = {"상태": "1시간 지각", "점수": 2}
            elif late_hours == 2:
                self.attendance_book[name] = {"상태": "2시간 지각", "점수": 1}
            elif late_hours >= 3:
                self.attendance_book[name] = {"상태": "결석 (3시간 이상 지각)", "점수": 0}
            else:
                print("⚠️ 잘못된 지각 시간입니다. 1 이상의 숫자를 입력하세요.\n")
                return
                
        elif attendance_type == '3':
            self.attendance_book[name] = {"상태": "결석", "점수": 0}
            
        else:
            print("⚠️ 잘못된 출석 유형입니다.\n")
            return
        
        status = self.attendance_book[name]["상태"]
        score = self.attendance_book[name]["점수"]
        print(f"✅ {name} 학생이 '{status}' 처리되어 {score}점이 부여되었습니다.")

    def show_attendance(self):
        """현재 전체 출석부 상태와 점수를 출력합니다."""
        print("\n=== 📝 현재 출석부 ===")
        if not self.attendance_book:
            print("등록된 학생이 없습니다.")
        else:
            for name, data in self.attendance_book.items():
                print(f"이름: {name}\t| 상태: {data['상태']}\t| 점수: {data['점수']}점")
        print("======================\n")


def main():
    manager = AttendanceManager()
    
    while True:
        print("\n[ 출석 관리 프로그램 ]")
        print("1. 학생 추가")
        print("2. 출석 체크 ")
        print("3. 출석부 확인")
        print("4. 프로그램 종료")
        
        choice = input("원하는 작업의 번호를 선택하세요: ")
        print("-" * 45)
        
        if choice == '1':
            name = input("등록할 학생 이름을 입력하세요: ")
            manager.add_student(name)
            
        elif choice == '2':
            print("\n=== 🔄 연속 출석 체크를 시작합니다 ===")
            print("(메인 메뉴로 돌아가려면 이름에 '0'을 입력하세요)")
            
            # 연속 출석 체크를 위한 내부 루프
            while True:
                name = input("\n출석을 체크할 학생 이름 ('0' 입력 시 종료): ")
                
                # '0'을 입력하면 연속 출석 체크 종료
                if name == '0':
                    print("연속 출석 체크를 종료하고 메인 메뉴로 돌아갑니다.\n")
                    break
                
                if name not in manager.attendance_book:
                    print(f"⚠️ 등록되지 않은 학생입니다: {name}")
                    continue

                print("[ 출석 유형 선택 ]")
                print("1. 정상 출석 (3점) | 2. 지각 (차감) | 3. 결석 (0점)")
                attendance_type = input("유형을 선택하세요 (1, 2, 3): ")
                
                if attendance_type == '1':
                    manager.mark_attendance(name, attendance_type)
                    
                elif attendance_type == '2':
                    try:
                        late_hours = int(input("몇 시간 지각했나요? (1, 2, 3 이상): "))
                        if late_hours <= 0:
                            print("⚠️ 지각 시간은 1 이상이어야 합니다.")
                        else:
                            manager.mark_attendance(name, attendance_type, late_hours)
                    except ValueError:
                        print("⚠️ 숫자로만 입력해주세요.")
                        
                elif attendance_type == '3':
                    manager.mark_attendance(name, attendance_type)
                    
                else:
                    print("⚠️ 1, 2, 3 중 하나를 입력해주세요.")
            
        elif choice == '3':
            manager.show_attendance()
            
        elif choice == '4':
            print("프로그램을 종료합니다. 수고하셨습니다!")
            break
            
        else:
            print("⚠️ 잘못된 입력입니다. 1~4 사이의 번호를 입력해주세요.\n")

if __name__ == "__main__":
    main()
