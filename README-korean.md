# Ren'Py 레이아웃 도구

![Version: Beta](https://img.shields.io/badge/Version-Beta-blue) 
![License: MIT](https://img.shields.io/badge/License-MIT-green)

> 이미지와 UI 요소를 화면에 적절히 배치할 수 있도록 돕는 시각 프리뷰 에디터

<img src="https://github.com/user-attachments/assets/50270935-7d56-4e37-beda-07d35281df5e" width="400"/>


## 개요 (Overview)


새 이미지를 현재 장면에 오버레이로 직접 로드하여, 게임 끄지 않고도 위치를 쉽게 보면서 바꿀 수 있게 해줍니다.

이 도구는 **미리 보기**만 됩니다. 코드를 직접 바꾸진 않지만, 여러 그림이나 UI가 화면에 잘 어울리는지 미리 확인하는 데 도움이 됩니다.

현재 베타 버전이며, 사용자 피드백에 따라 업데이트될 수 있습니다.

## 동작 영상 (Preview)

Video1 : [https://youtu.be/f3nDPWE2CIc](https://youtu.be/f3nDPWE2CIc)

Video2 : [https://youtu.be/MNqknAaeDuE](https://youtu.be/MNqknAaeDuE)


## ✨ 기능 (Features)

* 🖱️ **드래그 좌표 추적:** 이미지를 드래그하며 실시간 좌표 확인  
* 📂 **이미지 로딩 지원:** 파일 경로 및 Ren'Py 이미지 객체 모두 불러오기 가능  
* 🌗 **반투명 필터 토글:** 밝기/어둡기 전환으로 미리보기 화면 구분  
* ✨ **이미지 강조 표시:** 클릭 또는 드래그 시 윤곽선으로 선택 이미지 강조 (outline_shader 적용 시)  
* 🖼️ **다중 요소 배치:** 여러 이미지나 UI 요소를 동시에 추가 가능  
* 🗑️ **드래그로 삭제:** 이미지를 휴지통 아이콘에 드래그해 간편하게 제거  


## 🖼️ 설치 및 사용 가이드

Ren'Py의 `layout_tool`을 사용하면 이미지를 드래그하여 화면에 시각적으로 배치하거나 UI 요소를 조절할 수 있습니다. 
이 도구는 대화 재생과 같은 상호 작용을 일시적으로 중지하고 현재 화면을 기준으로 새로운 이미지 배치를 세밀하게 조정할 수 있도록 합니다.

### 설치

- 다운로드 또는 압축 해제 후 `game/` 폴더 아래 `layout-visualizer/` 폴더를 넣으세요. 
- 이 폴더 안에 `bin.png`와 `layout_tool.rpy` 파일이 있는지 확인하세요.

### 사용법

1. **도구 열기**:
   - 게임 실행 중 `L` 키로 켜고 `ESC`로 끕니다.
   - 반투명한 프리뷰 배경 위에서 UI 배치를 조절하세요.

2. **이미지 추가**:
   - 오른쪽 상단 `검색창`에 이미지 이름이나 경로를 입력하고 `Enter`를 누르세요.
   - 이미지를 드래그하면 `실시간 좌표가 표시`되며, 이를 코드에 바로 적용할 수 있습니다.
   - `Ren'Py transform (애니메이션 포함)이 적용된 이미지`를 로드할 수 있어, 정확한 인게임 위치를 반영합니다.

3. **이미지 제거**: `휴지통 아이콘`으로 이미지를 드래그하면 됩니다. 


## ⚠️ 주의 사항

이미지가 컨테이너(예: `frame`, `vbox`, `hbox`, `viewport`) 내부에 있거나 이미 위치 관련 속성을 가지고 있는 경우, 도구에 표시되는 최종 위치가 다른 레이아웃 규칙과의 중첩으로 인해 실제 배치와 다를 수 있습니다.

**해결책:**

* 이미지에서 모든 위치 속성을 제거하세요.

* 이미지를 `fixed` 컨테이너에 배치하세요.
  * `fixed` 컨테이너는 다른 레이아웃 요소의 간섭 없이 절대적인 고정 위치를 지정해줍니다.

**예시:**

다음은 `fixed` 컨테이너를 사용하여, 이미지가 다른 레이아웃 요소의 영향을 받지 않고 올바르게 배치되도록 하는 예시입니다:

```renpy
screen example_fixed:
    fixed:
        add "example_image.png" xpos 400 ypos 300
```

이 예시에서 이미지는 `xpos 400` 및 `ypos 300`의 고정 위치에 배치되며 다른 레이아웃 규칙의 영향을 받지 않습니다.

## 선택 사항: 외곽선 강조 효과 활성화하는 법 (데모 영상처럼)

🔗 <https://feniksdev.itch.io/outline-shader-renpy>

이 도구는 선택적으로 Fen의 아웃라인 셰이더를 지원합니다. 

데모 영상에서 나온 것과 같이, 현재 선택된 이미지에 대한 외곽선 강조 효과를 원한다면 FeniksDev의 아웃라인 셰이더 애셋을 다운로드하세요. 
효과를 활성화하려면 `layout_tool.rpy` 파일에서 다음 줄을 찾아 각 줄의 시작 부분에 있는 `#`을 제거하세요:

```renpy
# default item_active_trans = glow_outline(12, "#11d427", num_passes=6)
# default item_hover_trans = glow_outline(12, "#f5b5c0", num_passes=3)
```

아웃라인 셰이더를 사용하지 않으려면, 이 줄들이 `None`으로 설정되어 있는지 확인하세요:

```renpy
default item_active_trans = None
default item_hover_trans = None
```

## 파일 이동 관련

나중에 `layout_tool.rpy` 파일이나 `bin.png` 이미지를 다른 위치로 이동하는 경우, `layout_tool.rpy` 내에서 이미지 경로를 업데이트해야 합니다. 

파일을 열고 상단에 있는 `define bin_img` 줄을 확인하여 `bin.png`의 경로가 올바른지 확인하세요.

## 공지

* **기여 및 풀 리퀘스트:** 환영합니다!
* **문제 발생 시:** 문제가 발생하면 알려주세요. 이 버전은 요청에 따라 공개되었으며, 향후 업데이트 및 수정이 이루어질 수 있습니다.
