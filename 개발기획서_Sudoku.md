# Sudoku 게임 개발 기획서

## 프로젝트 개요

**게임명**: Sudoku Master (스도쿠 마스터)  
**장르**: 퍼즐 게임  
**플랫폼**: PC (Python/PyGame)  
**개발 기간**: 5주  
**개발 목적**: 포트폴리오용 퍼즐 게임 개발 프로젝트  
**개발 방법론**: **객체지향 프로그래밍(OOP) 원칙 엄격 준수** ⚠️

**컨셉**: 클래식 9x9 스도쿠 퍼즐 게임. 난이도 선택, 힌트 기능, 실행 취소/다시 실행 지원

---

## ⚠️ 필수 개발 원칙: 객체지향 프로그래밍 (OOP)

### 중요도: 🔴 CRITICAL - 준수하지 않으면 프로젝트 실패

본 프로젝트는 **객체지향 프로그래밍(OOP) 원칙을 엄격히 준수**하여 개발해야 합니다.

**이유**:
- 복잡한 퍼즐 로직을 모듈화하여 관리
- 확장 가능한 구조 (다양한 퍼즐 타입 추가 가능)
- 전문적인 개발 역량 증명
- 포트폴리오 품질 보증

**적용 원칙**:
1. ✅ **캡슐화(Encapsulation)**: 보드 상태와 퍼즐 로직을 클래스 내부에 은닉
2. ✅ **상속(Inheritance)**: 공통 UI 컴포넌트를 부모 클래스로 추상화
3. ✅ **다형성(Polymorphism)**: 난이도별 전략을 동일 인터페이스로 처리
4. ✅ **추상화(Abstraction)**: 퍼즐 생성/검증 알고리즘을 인터페이스로 정의

**SOLID 원칙**:
- **S**ingle Responsibility: 각 클래스는 단일 책임만
- **O**pen/Closed: 새 난이도 추가 시 기존 코드 수정 최소화
- **L**iskov Substitution: 난이도 전략을 교체 가능하게
- **I**nterface Segregation: 작고 구체적인 인터페이스
- **D**ependency Inversion: 구체적 구현이 아닌 추상화에 의존

---

## 1. 개발 목적

- **복잡한 로직 구현 능력 증명**: 스도쿠 생성/검증 알고리즘은 백트래킹, 재귀, 제약 전파 등 고급 알고리즘 필요
- **OOP 설계 능력 강화**: Board, Cell, Validator, Solver 등 명확한 책임 분리
- **알고리즘 역량 증명**: 퍼즐 생성 (백트래킹), 유효성 검사 (제약 체크), 힌트 제공
- **디자인 패턴 적용**: Strategy, Command, Observer 패턴 실전 활용
- **사용자 경험 설계**: 직관적인 UI/UX로 퍼즐 게임의 재미 극대화
- **포트폴리오 다양성**: 액션 게임과 차별화되는 논리 퍼즐 게임

---

## 2. 주요 기능 및 제공 가치

### 핵심 게임플레이
- **9x9 스도쿠 보드**: 81개 셀로 구성된 클래식 스도쿠
- **난이도 선택**: 쉬움(40개 제공), 보통(30개 제공), 어려움(25개 제공)
- **입력 시스템**:
  - 마우스 클릭으로 셀 선택
  - 키보드 숫자(1-9)로 값 입력
  - ESC 또는 Delete로 값 지우기
- **자동 유효성 검사**: 입력 즉시 규칙 위반 표시
- **힌트 기능**: 막힐 때 정답 셀 하나 공개
- **실행 취소/다시 실행**: 무제한 Undo/Redo
- **타이머**: 플레이 시간 측정
- **자동 저장**: 게임 진행 상황 저장

### 스도쿠 규칙
1. **행(Row)**: 각 행에 1-9 숫자가 중복 없이 배치
2. **열(Column)**: 각 열에 1-9 숫자가 중복 없이 배치
3. **3x3 박스(Box)**: 9개의 3x3 영역 각각에 1-9 숫자가 중복 없이 배치

### 제공 가치
- **두뇌 훈련**: 논리적 사고력 향상
- **집중력 강화**: 문제 해결에 몰입
- **성취감**: 퍼즐 완성 시 만족감
- **무한 재생 가능**: 매번 새로운 퍼즐 생성
- **접근성**: 언제 어디서나 즐길 수 있는 퍼즐

---

## 3. 개발 단계별 마일스톤

### Phase 1: 기본 보드 및 UI (1주차)

#### 작업 항목
- [ ] 프로젝트 구조 생성
- [ ] `config.py` 작성 (게임 상수 정의)
- [ ] `Cell` 클래스 구현 ⭐ **OOP**
  - [ ] Private 속성 (_value, _is_given, _is_valid)
  - [ ] Public 메서드 (set_value, get_value, is_empty)
  - [ ] Property로 읽기 전용 접근
  - [ ] 초기값/사용자 입력 구분
- [ ] `Board` 클래스 구현 ⭐ **OOP - 캡슐화**
  - [ ] Private 2차원 배열 (_cells)
  - [ ] get_cell(row, col) 메서드
  - [ ] set_cell(row, col, value) 메서드
  - [ ] clear_cell(row, col) 메서드
  - [ ] 보드 상태 캡슐화
- [ ] `Game` 클래스 기본 구조
  - [ ] PyGame 초기화
  - [ ] 메인 게임 루프
  - [ ] 이벤트 처리 (마우스/키보드)
- [ ] UI 렌더링
  - [ ] 9x9 그리드 그리기
  - [ ] 3x3 박스 구분선 (굵은 선)
  - [ ] 셀 선택 하이라이트
  - [ ] 숫자 표시

#### OOP 체크리스트 ⚠️ 필수 확인
- [ ] **캡슐화**: Cell의 _value가 private, 외부에서 set_value()로만 접근
- [ ] **캡슐화**: Board의 _cells가 private, get_cell()로만 접근
- [ ] **단일 책임**: Cell은 셀 상태만, Board는 보드 관리만
- [ ] **Property 패턴**: Cell.value를 읽기 전용으로 노출
- [ ] **명확한 인터페이스**: Public/Private 메서드 구분

#### Definition of Done
- ✅ 9x9 그리드가 화면에 표시됨
- ✅ 마우스 클릭으로 셀 선택 가능
- ✅ 키보드 숫자 입력으로 셀에 값 설정
- ✅ 선택된 셀이 하이라이트됨
- ✅ ESC로 게임 종료 가능
- ✅ **OOP 체크리스트 모두 통과**

#### 예상 소요 시간
- Cell 클래스: 2시간 ⭐ **OOP**
- Board 클래스: 3시간 ⭐ **OOP**
- Game 클래스 기본: 2시간
- UI 렌더링: 3시간
**총 10시간**

---

### Phase 2: 유효성 검사 시스템 (2주차)

#### 작업 항목
- [ ] `Validator` 클래스 구현 ⭐ **OOP - 단일 책임**
  - [ ] is_valid_move(board, row, col, num) 메서드
  - [ ] check_row(board, row, num) private 메서드
  - [ ] check_column(board, col, num) private 메서드
  - [ ] check_box(board, row, col, num) private 메서드
  - [ ] 검증 로직 캡슐화
- [ ] Board 클래스에 Validator 통합
  - [ ] Validator 의존성 주입
  - [ ] set_cell() 메서드에 유효성 검사 추가
  - [ ] 유효하지 않은 입력 시 에러 표시
- [ ] Cell 클래스 확장
  - [ ] _is_valid 상태 추가
  - [ ] mark_invalid() 메서드
  - [ ] mark_valid() 메서드
- [ ] UI 피드백
  - [ ] 유효하지 않은 셀을 빨간색으로 표시
  - [ ] 동일 숫자가 있는 행/열/박스 하이라이트
  - [ ] 에러 메시지 표시 (선택 사항)
- [ ] 게임 완료 감지
  - [ ] is_board_full() 메서드
  - [ ] is_board_solved() 메서드
  - [ ] 승리 조건 체크

#### OOP 체크리스트 ⚠️ 필수 확인
- [ ] **단일 책임**: Validator는 검증만 담당
- [ ] **캡슐화**: 검증 로직이 private 메서드로 숨김
- [ ] **의존성 주입**: Board가 Validator를 주입받음
- [ ] **인터페이스 분리**: Validator가 하나의 목적만 가짐
- [ ] **메서드 분리**: check_row, check_column, check_box 독립적

#### Definition of Done
- ✅ 입력 시 즉시 유효성 검사
- ✅ 유효하지 않은 입력은 빨간색 표시
- ✅ 같은 행/열/박스의 중복 숫자 감지
- ✅ 보드가 완성되면 승리 메시지 표시
- ✅ **OOP 체크리스트 모두 통과**

#### 예상 소요 시간
- Validator 클래스: 3시간 ⭐ **OOP**
- Board 통합: 2시간
- Cell 확장: 1시간
- UI 피드백: 2시간
- 게임 완료 감지: 2시간
**총 10시간**

---

### Phase 3: 퍼즐 생성 시스템 (3주차)

#### 작업 항목
- [ ] `Solver` 클래스 구현 ⭐ **OOP - 단일 책임**
  - [ ] solve(board) 메서드 (백트래킹 알고리즘)
  - [ ] find_empty_cell(board) private 메서드
  - [ ] is_safe(board, row, col, num) private 메서드
  - [ ] 재귀적 백트래킹 구현
- [ ] `PuzzleGenerator` 클래스 구현 ⭐ **OOP - Factory Pattern**
  - [ ] generate(difficulty) 메서드
  - [ ] _create_full_board() private 메서드 (완성된 보드 생성)
  - [ ] _remove_numbers(board, difficulty) private 메서드
  - [ ] _has_unique_solution(board) private 메서드
  - [ ] Factory Method로 난이도별 퍼즐 생성
- [ ] `DifficultyStrategy` 추상 클래스 ⭐ **OOP - Strategy Pattern**
  - [ ] get_cells_to_remove() 추상 메서드
  - [ ] EasyStrategy (40개 제공)
  - [ ] MediumStrategy (30개 제공)
  - [ ] HardStrategy (25개 제공)
- [ ] 난이도 선택 UI
  - [ ] 시작 화면에 난이도 버튼
  - [ ] 선택된 난이도 표시
- [ ] 새 게임 시작
  - [ ] "New Game" 버튼
  - [ ] 보드 초기화
  - [ ] 새 퍼즐 생성

#### OOP 체크리스트 ⚠️ 필수 확인
- [ ] **단일 책임**: Solver는 해결만, Generator는 생성만
- [ ] **Strategy Pattern**: 난이도별 전략 클래스 분리
- [ ] **Factory Pattern**: generate()가 난이도별 퍼즐 생성
- [ ] **개방-폐쇄**: 새 난이도 추가 시 기존 코드 수정 없음
- [ ] **캡슐화**: 백트래킹 알고리즘 내부 구현 숨김
- [ ] **다형성**: 모든 Strategy를 동일 인터페이스로 처리

#### Definition of Done
- ✅ "New Game" 클릭 시 새 퍼즐 생성
- ✅ 난이도 선택 가능 (Easy, Medium, Hard)
- ✅ 생성된 퍼즐이 유일한 해를 가짐
- ✅ 초기 숫자는 수정 불가 (다른 색으로 표시)
- ✅ 백트래킹 알고리즘이 정상 작동
- ✅ **OOP 체크리스트 모두 통과**

#### 예상 소요 시간
- Solver 클래스 (백트래킹): 4시간 ⭐ **OOP**
- PuzzleGenerator 클래스: 4시간 ⭐ **OOP**
- DifficultyStrategy 구조: 3시간 ⭐ **OOP - Strategy**
- 난이도 선택 UI: 2시간
**총 13시간**

---

### Phase 4: 고급 기능 (4주차)

#### 작업 항목
- [ ] `CommandHistory` 클래스 구현 ⭐ **OOP - Command Pattern**
  - [ ] Command 추상 클래스
  - [ ] SetCellCommand (셀 값 설정)
  - [ ] ClearCellCommand (셀 값 지우기)
  - [ ] execute() 메서드
  - [ ] undo() 메서드
  - [ ] redo() 메서드
  - [ ] 명령 스택 관리 (_history, _redo_stack)
- [ ] 실행 취소/다시 실행 구현
  - [ ] Ctrl+Z: Undo
  - [ ] Ctrl+Y: Redo
  - [ ] UI 버튼 추가
  - [ ] 명령 히스토리 제한 (최대 100개)
- [ ] `HintProvider` 클래스 ⭐ **OOP - 단일 책임**
  - [ ] get_hint(board, solver) 메서드
  - [ ] find_solvable_cell(board) private 메서드
  - [ ] Solver를 사용하여 정답 찾기
  - [ ] 힌트 제공 횟수 제한 (옵션)
- [ ] 타이머 구현
  - [ ] `Timer` 클래스
  - [ ] start(), pause(), resume(), reset()
  - [ ] get_elapsed_time() 메서드
  - [ ] UI에 시간 표시 (MM:SS)
- [ ] 자동 저장/불러오기
  - [ ] `SaveManager` 클래스 ⭐ **OOP**
  - [ ] save_game(board, timer) 메서드
  - [ ] load_game() 메서드
  - [ ] JSON 형식으로 저장
  - [ ] 게임 종료 시 자동 저장

#### OOP 체크리스트 ⚠️ 필수 확인
- [ ] **Command Pattern**: 모든 동작이 Command 객체로
- [ ] **단일 책임**: HintProvider는 힌트만, Timer는 시간 측정만
- [ ] **캡슐화**: 명령 히스토리가 CommandHistory에 숨김
- [ ] **다형성**: 다양한 Command를 동일하게 처리
- [ ] **의존성 주입**: HintProvider가 Solver를 주입받음
- [ ] **인터페이스 일관성**: 모든 Command가 execute/undo 구현

#### Definition of Done
- ✅ Ctrl+Z/Ctrl+Y로 실행 취소/다시 실행
- ✅ "Hint" 버튼 클릭 시 한 셀 자동 채워짐
- ✅ 타이머가 화면에 표시되고 정확히 작동
- ✅ 게임 진행 상황이 자동 저장됨
- ✅ 재시작 시 이전 게임 복구 가능
- ✅ **OOP 체크리스트 모두 통과**

#### 예상 소요 시간
- CommandHistory (Command Pattern): 4시간 ⭐ **OOP**
- HintProvider: 2시간 ⭐ **OOP**
- Timer: 2시간
- SaveManager: 3시간 ⭐ **OOP**
- UI 통합: 2시간
**총 13시간**

---

### Phase 5: 폴리싱 및 배포 (5주차)

#### 작업 항목
- [ ] UI/UX 개선
  - [ ] 숫자 입력 시 애니메이션
  - [ ] 셀 하이라이트 효과
  - [ ] 승리 애니메이션
  - [ ] 사운드 효과 (선택 사항)
- [ ] 통계 기능
  - [ ] `StatisticsManager` 클래스 ⭐ **OOP**
  - [ ] 게임 완료 횟수
  - [ ] 난이도별 최단 시간
  - [ ] 평균 플레이 시간
  - [ ] 힌트 사용 횟수
- [ ] 설정 메뉴
  - [ ] 테마 변경 (밝은/어두운 모드)
  - [ ] 사운드 On/Off
  - [ ] 자동 유효성 검사 On/Off
- [ ] **OOP 코드 품질 최종 점검** ⭐ **CRITICAL**
  - [ ] 모든 클래스가 단일 책임 원칙 준수
  - [ ] Private/Public 접근 제어 올바름
  - [ ] Strategy Pattern 정상 작동
  - [ ] Command Pattern 정상 작동
  - [ ] 캡슐화 충분히 이루어짐
  - [ ] Docstring 모든 클래스/메서드에 존재
  - [ ] 매직 넘버 없음
  - [ ] 중복 코드 없음
- [ ] 버그 수정 및 테스트
  - [ ] 경계값 테스트 (빈 보드, 완성 보드)
  - [ ] 퍼즐 생성 실패 처리
  - [ ] 메모리 누수 확인
- [ ] 문서화
  - [ ] README.md (OOP 설계 강조)
  - [ ] 알고리즘 설명 (백트래킹)
  - [ ] 클래스 다이어그램
  - [ ] requirements.txt
  - [ ] LICENSE (MIT)

#### OOP 최종 점검 체크리스트 ⚠️ 필수 확인
- [ ] **클래스 설계**: 모든 클래스가 명확한 책임
- [ ] **캡슐화**: 모든 속성이 private
- [ ] **디자인 패턴**: Strategy, Command, Factory 적용
- [ ] **SOLID 원칙**: 5가지 모두 준수
- [ ] **코드 품질**: 깨끗하고 읽기 쉬운 코드

#### Definition of Done
- ✅ 게임이 안정적으로 작동
- ✅ UI가 직관적이고 아름다움
- ✅ 모든 기능이 정상 작동
- ✅ README.md 완성
- ✅ **OOP 최종 점검 체크리스트 100% 통과** ⭐
- ✅ 포트폴리오로 제출 가능한 품질

#### 예상 소요 시간
- UI/UX 개선: 3시간
- 통계 기능: 3시간
- 설정 메뉴: 2시간
- **OOP 코드 품질 점검**: 4시간 ⭐ **CRITICAL**
- 버그 수정: 3시간
- 문서화: 3시간
**총 18시간**

---

## 4. 전체 일정

| 주차 | Phase | 핵심 작업 | 예상 시간 |
|------|-------|----------|----------|
| 1주차 | Phase 1 | 기본 보드 & UI | 10시간 |
| 2주차 | Phase 2 | 유효성 검사 | 10시간 |
| 3주차 | Phase 3 | 퍼즐 생성 (백트래킹) | 13시간 |
| 4주차 | Phase 4 | 고급 기능 (Undo/Hint) | 13시간 |
| 5주차 | Phase 5 | 폴리싱 & 배포 | 18시간 |
| **총계** | | | **64시간** |

---

## 5. 기술 스택

### 개발 환경
- **언어**: Python 3.8+
- **게임 엔진**: PyGame 2.5+
- **IDE**: VS Code / PyCharm
- **버전 관리**: Git + GitHub

### 라이브러리
```python
# requirements.txt
pygame==2.5.0
```

### 개발 도구
- **코드 품질**: pylint, black
- **테스트**: pytest (선택 사항)
- **문서화**: Sphinx (선택 사항)

---

## 6. 프로젝트 구조

```
sudoku/
├── main.py                 # 게임 실행 진입점
├── game.py                 # Game 클래스
├── board.py                # Board 클래스
├── cell.py                 # Cell 클래스
├── validator.py            # Validator 클래스
├── solver.py               # Solver 클래스 (백트래킹)
├── puzzle_generator.py     # PuzzleGenerator 클래스
├── strategies/
│   ├── __init__.py
│   ├── difficulty_strategy.py  # 추상 Strategy
│   ├── easy_strategy.py
│   ├── medium_strategy.py
│   └── hard_strategy.py
├── commands/
│   ├── __init__.py
│   ├── command.py          # Command 추상 클래스
│   ├── set_cell_command.py
│   └── clear_cell_command.py
├── managers/
│   ├── __init__.py
│   ├── command_history.py  # CommandHistory 클래스
│   ├── hint_provider.py    # HintProvider 클래스
│   ├── timer.py            # Timer 클래스
│   ├── save_manager.py     # SaveManager 클래스
│   └── statistics_manager.py
├── ui/
│   ├── __init__.py
│   ├── renderer.py         # UI 렌더링
│   └── button.py           # Button 클래스
├── config.py               # 게임 설정 상수
├── assets/                 # 게임 리소스
│   ├── fonts/
│   └── sounds/
├── data/                   # 저장 데이터
│   ├── save_game.json
│   └── statistics.json
├── tests/                  # 테스트 코드
│   ├── test_validator.py
│   ├── test_solver.py
│   └── test_generator.py
├── requirements.txt
├── README.md
└── LICENSE
```

---

## 7. 핵심 클래스 설계 (OOP 원칙 적용)

### 🔴 OOP 설계 필수 준수사항

**모든 클래스는 다음 원칙을 반드시 따라야 함**:
1. **단일 책임 원칙(SRP)**: 각 클래스는 하나의 책임만
2. **캡슐화**: private 속성(_변수명), public 메서드로 접근
3. **명확한 인터페이스**: 외부에서 호출할 메서드만 public

---

### 7.1 Cell 클래스 (셀 하나)
**책임**: 개별 셀의 상태 관리

```python
class Cell:
    """
    스도쿠 보드의 한 셀을 나타내는 클래스
    - 값 저장 (1-9 또는 비어있음)
    - 초기값/사용자 입력 구분
    - 유효성 상태 관리
    """
    
    def __init__(self, value=0, is_given=False):
        self._value = value           # private: 셀 값
        self._is_given = is_given     # private: 초기 제공 값인지
        self._is_valid = True         # private: 유효성 상태
    
    # Public 인터페이스
    def set_value(self, value):
        """값 설정 (1-9 또는 0)"""
        if not self._is_given:
            self._value = value
    
    def clear(self):
        """값 지우기"""
        if not self._is_given:
            self._value = 0
    
    def mark_invalid(self):
        """유효하지 않음으로 표시"""
        self._is_valid = False
    
    def mark_valid(self):
        """유효함으로 표시"""
        self._is_valid = True
    
    # Property (읽기 전용)
    @property
    def value(self):
        return self._value
    
    @property
    def is_given(self):
        return self._is_given
    
    @property
    def is_valid(self):
        return self._is_valid
    
    @property
    def is_empty(self):
        return self._value == 0
```

**OOP 원칙 적용**:
- ✅ **캡슐화**: 모든 속성 private
- ✅ **Property**: 읽기 전용 접근 제공
- ✅ **단일 책임**: 셀 상태만 관리

---

### 7.2 Board 클래스 (9x9 보드)
**책임**: 전체 스도쿠 보드 관리

```python
class Board:
    """
    9x9 스도쿠 보드 클래스
    - 81개 Cell 객체 관리
    - 셀 접근 인터페이스 제공
    - 보드 상태 캡슐화
    """
    
    def __init__(self):
        # Private: 9x9 Cell 배열
        self._cells = [[Cell() for _ in range(9)] for _ in range(9)]
        self._validator = None  # Validator 의존성 주입
    
    def set_validator(self, validator):
        """Validator 주입 (의존성 주입)"""
        self._validator = validator
    
    # Public 인터페이스
    def get_cell(self, row, col):
        """셀 가져오기"""
        return self._cells[row][col]
    
    def set_cell(self, row, col, value):
        """셀 값 설정 (유효성 검사 포함)"""
        cell = self._cells[row][col]
        
        if cell.is_given:
            return False  # 초기값은 수정 불가
        
        # 유효성 검사
        if self._validator and not self._validator.is_valid_move(
            self, row, col, value
        ):
            cell.mark_invalid()
            return False
        
        cell.set_value(value)
        cell.mark_valid()
        return True
    
    def clear_cell(self, row, col):
        """셀 값 지우기"""
        self._cells[row][col].clear()
    
    def is_full(self):
        """보드가 꽉 찼는지 확인"""
        for row in range(9):
            for col in range(9):
                if self._cells[row][col].is_empty:
                    return False
        return True
    
    def reset(self):
        """보드 초기화"""
        for row in range(9):
            for col in range(9):
                if not self._cells[row][col].is_given:
                    self._cells[row][col].clear()
```

**OOP 원칙 적용**:
- ✅ **캡슐화**: _cells 직접 접근 불가
- ✅ **의존성 주입**: Validator를 주입받음
- ✅ **단일 책임**: 보드 관리만

---

### 7.3 Validator 클래스 (유효성 검사)
**책임**: 스도쿠 규칙 검증

```python
class Validator:
    """
    스도쿠 유효성 검사 클래스
    - 행/열/박스 규칙 검증
    - 승리 조건 확인
    """
    
    def is_valid_move(self, board, row, col, num):
        """숫자가 유효한지 검사"""
        if num == 0:  # 빈 칸은 항상 유효
            return True
        
        return (self._check_row(board, row, num) and
                self._check_column(board, col, num) and
                self._check_box(board, row, col, num))
    
    def is_board_solved(self, board):
        """보드가 올바르게 완성되었는지 확인"""
        if not board.is_full():
            return False
        
        for row in range(9):
            for col in range(9):
                cell = board.get_cell(row, col)
                if not self.is_valid_move(board, row, col, cell.value):
                    return False
        return True
    
    # Private 메서드 (내부 구현)
    def _check_row(self, board, row, num):
        """행 중복 검사"""
        for col in range(9):
            cell = board.get_cell(row, col)
            if cell.value == num:
                return False
        return True
    
    def _check_column(self, board, col, num):
        """열 중복 검사"""
        for row in range(9):
            cell = board.get_cell(row, col)
            if cell.value == num:
                return False
        return True
    
    def _check_box(self, board, row, col, num):
        """3x3 박스 중복 검사"""
        box_row = (row // 3) * 3
        box_col = (col // 3) * 3
        
        for r in range(box_row, box_row + 3):
            for c in range(box_col, box_col + 3):
                cell = board.get_cell(r, c)
                if cell.value == num:
                    return False
        return True
```

**OOP 원칙 적용**:
- ✅ **단일 책임**: 검증만 담당
- ✅ **캡슐화**: 내부 로직 private
- ✅ **메서드 분리**: 행/열/박스 각각 독립

---

### 7.4 Solver 클래스 (백트래킹)
**책임**: 스도쿠 퍼즐 해결

```python
class Solver:
    """
    백트래킹 알고리즘으로 스도쿠 해결
    - 재귀적 탐색
    - 유일해 존재 여부 확인
    """
    
    def __init__(self, validator):
        self._validator = validator  # Validator 의존성
    
    def solve(self, board):
        """보드 해결 (백트래킹)"""
        empty_cell = self._find_empty_cell(board)
        
        if not empty_cell:
            return True  # 모든 셀이 채워짐
        
        row, col = empty_cell
        
        for num in range(1, 10):
            if self._validator.is_valid_move(board, row, col, num):
                board.set_cell(row, col, num)
                
                if self.solve(board):
                    return True
                
                board.clear_cell(row, col)  # 백트래킹
        
        return False
    
    def has_unique_solution(self, board):
        """유일한 해가 있는지 확인"""
        # 구현 생략 (두 개 이상의 해 찾기)
        pass
    
    # Private
    def _find_empty_cell(self, board):
        """비어있는 셀 찾기"""
        for row in range(9):
            for col in range(9):
                if board.get_cell(row, col).is_empty:
                    return (row, col)
        return None
```

**OOP 원칙 적용**:
- ✅ **단일 책임**: 해결만 담당
- ✅ **의존성 주입**: Validator 주입
- ✅ **재귀 알고리즘**: 백트래킹

---

### 7.5 DifficultyStrategy (추상 클래스)
**책임**: 난이도별 전략 정의

```python
from abc import ABC, abstractmethod

class DifficultyStrategy(ABC):
    """난이도 전략 추상 클래스"""
    
    @abstractmethod
    def get_cells_to_remove(self):
        """제거할 셀 개수 반환"""
        pass

class EasyStrategy(DifficultyStrategy):
    def get_cells_to_remove(self):
        return 40  # 41개 제공

class MediumStrategy(DifficultyStrategy):
    def get_cells_to_remove(self):
        return 51  # 30개 제공

class HardStrategy(DifficultyStrategy):
    def get_cells_to_remove(self):
        return 56  # 25개 제공
```

**OOP 원칙 적용**:
- ✅ **Strategy Pattern**: 난이도별 전략
- ✅ **개방-폐쇄**: 새 난이도 추가 쉬움
- ✅ **다형성**: 모든 전략을 동일하게 처리

---

### 7.6 PuzzleGenerator 클래스
**책임**: 퍼즐 생성 (Factory Pattern)

```python
class PuzzleGenerator:
    """
    스도쿠 퍼즐 생성기
    - 완성된 보드 생성
    - 난이도에 따라 숫자 제거
    """
    
    def __init__(self, solver):
        self._solver = solver
    
    def generate(self, difficulty_strategy):
        """
        퍼즐 생성 (Factory Method)
        :param difficulty_strategy: DifficultyStrategy 객체
        """
        board = self._create_full_board()
        cells_to_remove = difficulty_strategy.get_cells_to_remove()
        self._remove_numbers(board, cells_to_remove)
        return board
    
    # Private
    def _create_full_board(self):
        """완성된 보드 생성"""
        board = Board()
        # 랜덤하게 숫자 배치 후 solve
        # ... 구현 생략
        return board
    
    def _remove_numbers(self, board, count):
        """숫자 제거 (유일해 유지)"""
        # ... 구현 생략
        pass
```

**OOP 원칙 적용**:
- ✅ **Factory Pattern**: generate()
- ✅ **Strategy Pattern 활용**: 난이도 전략 주입
- ✅ **캡슐화**: 생성 로직 숨김

---

### 7.7 Command 클래스 (Command Pattern)
**책임**: 동작을 객체로 캡슐화

```python
from abc import ABC, abstractmethod

class Command(ABC):
    """명령 추상 클래스"""
    
    @abstractmethod
    def execute(self):
        pass
    
    @abstractmethod
    def undo(self):
        pass

class SetCellCommand(Command):
    """셀 값 설정 명령"""
    
    def __init__(self, board, row, col, new_value):
        self._board = board
        self._row = row
        self._col = col
        self._new_value = new_value
        self._old_value = board.get_cell(row, col).value
    
    def execute(self):
        self._board.set_cell(self._row, self._col, self._new_value)
    
    def undo(self):
        self._board.set_cell(self._row, self._col, self._old_value)

class CommandHistory:
    """명령 히스토리 관리"""
    
    def __init__(self):
        self._history = []
        self._redo_stack = []
    
    def execute(self, command):
        command.execute()
        self._history.append(command)
        self._redo_stack.clear()
    
    def undo(self):
        if self._history:
            command = self._history.pop()
            command.undo()
            self._redo_stack.append(command)
    
    def redo(self):
        if self._redo_stack:
            command = self._redo_stack.pop()
            command.execute()
            self._history.append(command)
```

**OOP 원칙 적용**:
- ✅ **Command Pattern**: 동작을 객체로
- ✅ **캡슐화**: 히스토리 관리 숨김
- ✅ **다형성**: 다양한 명령 처리

---

### 7.8 클래스 다이어그램

```
Cell (셀)
    - value, is_given, is_valid

Board (보드)
    - cells[][]
    - validator
    ├─> Cell (81개)
    └─> Validator

Validator (검증)
    - is_valid_move()

Solver (해결)
    - validator
    - solve() (백트래킹)

DifficultyStrategy (추상)
    ├─> EasyStrategy
    ├─> MediumStrategy
    └─> HardStrategy

PuzzleGenerator (생성)
    - solver
    - generate(strategy)

Command (추상)
    ├─> SetCellCommand
    └─> ClearCellCommand

CommandHistory
    - history[]
    - redo_stack[]

Game (게임 총괄)
    ├─> Board
    ├─> Validator
    ├─> Solver
    ├─> PuzzleGenerator
    └─> CommandHistory
```

---

## 8. 게임 설정 상수 (config.py)

```python
# 화면 설정
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 700
FPS = 60

# 보드 설정
BOARD_SIZE = 9
BOX_SIZE = 3
CELL_SIZE = 60
BOARD_OFFSET_X = 30
BOARD_OFFSET_Y = 100

# 색상
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
LIGHT_BLUE = (200, 220, 255)
DARK_BLUE = (100, 150, 255)
RED = (255, 100, 100)
GREEN = (100, 255, 100)

# 셀 색상
CELL_GIVEN_COLOR = (50, 50, 50)      # 초기 숫자 (진한 회색)
CELL_USER_COLOR = (0, 100, 200)      # 사용자 입력 (파란색)
CELL_INVALID_COLOR = (255, 50, 50)   # 유효하지 않음 (빨간색)
CELL_SELECTED_COLOR = (255, 255, 150) # 선택된 셀 (노란색)

# 난이도
EASY_CELLS_TO_REMOVE = 40
MEDIUM_CELLS_TO_REMOVE = 51
HARD_CELLS_TO_REMOVE = 56

# 폰트
FONT_SIZE_CELL = 40
FONT_SIZE_UI = 24
```

---

## 9. 핵심 알고리즘 상세

### 9.1 백트래킹 (Backtracking) - 퍼즐 해결

**개념**: 재귀적으로 가능한 숫자를 시도하고, 막히면 되돌아가는 방식

```python
def solve(board):
    """
    백트래킹으로 스도쿠 해결
    시간복잡도: O(9^(빈셀개수)) - 최악의 경우
    """
    # 1. 빈 셀 찾기
    empty = find_empty_cell(board)
    if not empty:
        return True  # 모든 셀이 채워짐 = 완성
    
    row, col = empty
    
    # 2. 1-9까지 시도
    for num in range(1, 10):
        # 3. 유효한지 확인
        if is_valid_move(board, row, col, num):
            # 4. 숫자 배치
            board[row][col] = num
            
            # 5. 재귀 호출
            if solve(board):
                return True
            
            # 6. 백트래킹 (실패 시 되돌리기)
            board[row][col] = 0
    
    return False  # 모든 숫자 시도 실패
```

**예시**:
```
[5, 3, ?, ...]  → 1 시도 → 실패
                → 2 시도 → 실패
                → 3 시도 → 충돌
                → 4 시도 → 성공! → 다음 셀
```

---

### 9.2 퍼즐 생성 알고리즘

**단계**:
1. **완성된 보드 생성**
   - 빈 보드에서 시작
   - 랜덤하게 숫자 배치 (일부만)
   - 백트래킹으로 완성

2. **숫자 제거**
   - 난이도에 따라 N개 셀 제거
   - 제거 후 유일한 해가 있는지 확인
   - 유일하지 않으면 다시 시도

```python
def generate_puzzle(difficulty):
    """퍼즐 생성"""
    # 1. 완성된 보드 생성
    board = create_full_board()
    
    # 2. 숫자 제거
    cells_to_remove = get_cells_to_remove(difficulty)
    positions = list of all (row, col)
    random.shuffle(positions)
    
    for row, col in positions[:cells_to_remove]:
        temp = board[row][col]
        board[row][col] = 0
        
        # 유일한 해 확인
        if not has_unique_solution(board):
            board[row][col] = temp  # 복구
    
    return board
```

---

### 9.3 유일한 해 확인

```python
def has_unique_solution(board):
    """두 개 이상의 해가 있는지 확인"""
    solution_count = [0]  # 해 개수 (참조로 전달)
    
    def count_solutions(board, count):
        if count[0] > 1:  # 이미 2개 이상 발견
            return
        
        empty = find_empty_cell(board)
        if not empty:
            count[0] += 1
            return
        
        row, col = empty
        for num in range(1, 10):
            if is_valid(board, row, col, num):
                board[row][col] = num
                count_solutions(board, count)
                board[row][col] = 0
    
    count_solutions(board.copy(), solution_count)
    return solution_count[0] == 1
```

---

## 10. 테스트 체크리스트

### 기능 테스트
- [ ] 보드가 정상적으로 렌더링됨
- [ ] 셀 클릭 시 선택됨
- [ ] 숫자 입력 시 셀에 표시됨
- [ ] 유효하지 않은 입력은 빨간색 표시
- [ ] 보드 완성 시 승리 메시지
- [ ] Undo/Redo 정상 작동
- [ ] Hint 버튼 클릭 시 힌트 제공
- [ ] 타이머 정상 작동
- [ ] 게임 저장/불러오기
- [ ] 난이도 선택 가능

### OOP 설계 테스트 ⭐ 필수
- [ ] **클래스 독립성**: 각 클래스 독립적 테스트 가능
- [ ] **캡슐화**: Private 속성 직접 접근 불가
- [ ] **Strategy Pattern**: 난이도 전략 교체 가능
- [ ] **Command Pattern**: Undo/Redo 정상 작동
- [ ] **의존성 주입**: Board에 Validator 주입 가능
- [ ] **단일 책임**: 각 클래스 수정 시 영향 최소화

### 알고리즘 테스트
- [ ] 백트래킹이 항상 해를 찾음
- [ ] 생성된 퍼즐이 유일한 해를 가짐
- [ ] 유효성 검사가 정확함
- [ ] 난이도가 적절함 (쉬움/보통/어려움)

### 코드 품질 테스트
- [ ] **Docstring**: 모든 클래스와 메서드
- [ ] **명명 규칙**: PascalCase, snake_case 일관성
- [ ] **매직 넘버**: config.py에 모두 정의
- [ ] **중복 코드**: 없음
- [ ] **메서드 길이**: 대부분 20줄 이하

### 엣지 케이스 테스트
- [ ] 빈 보드에서 solve 호출
- [ ] 이미 완성된 보드
- [ ] 해가 없는 보드 (에러 처리)
- [ ] 초기 숫자 수정 시도 (거부)
- [ ] Undo 스택이 비었을 때 Undo 시도

---

## 11. Git 브랜치 전략

```
main (안정 버전)
  ├── develop (개발 브랜치)
  │     ├── feature/phase1-board
  │     ├── feature/phase2-validation
  │     ├── feature/phase3-generator
  │     ├── feature/phase4-commands
  │     └── feature/phase5-polish
  └── release/v1.0
```

---

## 12. 개발 회의 안건

### 주간 체크포인트
- Phase 완료 여부 확인
- OOP 체크리스트 검토
- 코드 리뷰 (페어 프로그래밍)
- 다음 Phase 계획

### 리뷰 포인트
- 백트래킹 알고리즘 최적화
- 퍼즐 생성 속도 개선
- UI/UX 피드백
- 난이도 밸런싱

---

## 13. 리스크 관리

### 기술적 리스크

| 리스크 | 확률 | 영향 | 대응책 |
|--------|------|------|--------|
| 백트래킹 성능 저하 | 중 | 높음 | 최적화, 캐싱 |
| 퍼즐 생성 실패 | 중 | 중 | 재시도 로직, 타임아웃 |
| 유일해 검증 느림 | 중 | 중 | 휴리스틱 사용 |
| OOP 원칙 위반 | 낮 | 높음 | 주기적 코드 리뷰 |

---

## 부록 A: 참고 자료

### 알고리즘
- **백트래킹**: [Wikipedia](https://en.wikipedia.org/wiki/Backtracking)
- **스도쿠 생성**: [Algorithm Explained](https://dlbeer.co.nz/articles/sudoku.html)

### OOP 디자인 패턴
- **Strategy Pattern**: [Refactoring Guru](https://refactoring.guru/design-patterns/strategy)
- **Command Pattern**: [Refactoring Guru](https://refactoring.guru/design-patterns/command)

---

## 부록 B: OOP 가이드 종합 ⭐ CRITICAL

### 면접 대응 시나리오

**Q: "이 프로젝트에서 어떤 디자인 패턴을 사용했나요?"**

**A:**
> "세 가지 주요 디자인 패턴을 적용했습니다:
> 
> 1. **Strategy Pattern**: 난이도별 퍼즐 생성 전략을 DifficultyStrategy 추상 클래스로 정의하고, Easy/Medium/Hard 구현체를 만들었습니다. 새 난이도 추가 시 기존 코드 수정 없이 새 클래스만 추가하면 됩니다.
> 
> 2. **Command Pattern**: 모든 사용자 동작을 Command 객체로 캡슐화하여 Undo/Redo를 구현했습니다. SetCellCommand, ClearCellCommand 등이 있으며, CommandHistory가 명령 스택을 관리합니다.
> 
> 3. **Factory Method**: PuzzleGenerator의 generate() 메서드가 난이도 전략을 받아 적절한 퍼즐을 생성합니다.
> 
> 추가로 SOLID 원칙도 철저히 준수했습니다. 특히 단일 책임 원칙에 따라 Validator는 검증만, Solver는 해결만, Generator는 생성만 담당하도록 분리했습니다."

**Q: "백트래킹 알고리즘을 어떻게 최적화했나요?"**

**A:**
> "세 가지 최적화를 적용했습니다:
> 
> 1. **제약 전파(Constraint Propagation)**: 각 셀에서 가능한 숫자를 미리 계산하여 시도 횟수를 줄였습니다.
> 
> 2. **MRV(Minimum Remaining Values) 휴리스틱**: 가능한 숫자가 가장 적은 셀부터 채워 조기 실패를 유도했습니다.
> 
> 3. **조기 종료**: 유일한 해를 확인할 때, 2개 이상의 해를 발견하면 즉시 중단합니다.
> 
> 결과적으로 평균 퍼즐 생성 시간을 0.5초 이하로 줄였습니다."

---

## 부록 C: README 샘플

```markdown
# 🧩 Sudoku Master

> A professionally crafted Sudoku game demonstrating OOP principles and advanced algorithms

## 🎯 Highlights

- ✅ **Backtracking Algorithm** for puzzle generation and solving
- ✅ **Strategy Pattern** for difficulty levels
- ✅ **Command Pattern** for unlimited Undo/Redo
- ✅ **100% OOP Compliance** with SOLID principles

## 🏗️ Architecture

### Key Classes
- `Board`: Manages 9x9 grid with encapsulation
- `Validator`: Rule validation with single responsibility
- `Solver`: Backtracking algorithm implementation
- `PuzzleGenerator`: Factory method for puzzle creation
- `CommandHistory`: Command pattern for Undo/Redo

### Design Patterns
- **Strategy**: Difficulty levels (Easy/Medium/Hard)
- **Command**: User actions as objects
- **Factory Method**: Puzzle generation

## 🚀 Quick Start

```bash
python main.py
```

## 🧠 Algorithms

### Backtracking
- Recursive exploration of valid placements
- Early termination on conflicts
- O(9^empty_cells) complexity

### Puzzle Generation
1. Create complete board with randomization
2. Remove cells based on difficulty
3. Verify unique solution exists

## 📊 Statistics

- **Code Quality**: 95%+ test coverage
- **OOP Compliance**: 100%
- **Performance**: <0.5s puzzle generation
```

---

이제 OOP 원칙을 완벽히 적용한 스도쿠 게임 개발기획서가 준비되었습니다! 🎉
