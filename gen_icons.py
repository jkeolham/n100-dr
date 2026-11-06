#!/home/ttolmany/scripts/tide-alert/venv/bin/python3
"""N100 재해복구(DR) 관제 런북 PWA/파비콘 생성 스크립트.
디자인: 다크 네이비(#0d1117) 배경 + 블루 림 + 방패(Shield) + 번개(Lightning) 복구 모티브.
"""
import math
from pathlib import Path
from PIL import Image, ImageDraw

SIZE = 512
OUT_DIR = Path(__file__).resolve().parent

BG_COLOR = (13, 17, 23)        # #0d1117
RIM_COLOR = (48, 54, 61)       # #30363d
SHIELD_BG = (22, 27, 34)       # #161b22
SHIELD_BORDER = (88, 166, 255) # #58a6ff
BOLT_COLOR = (210, 153, 34)    # #d29922 (골드 옐로우)
BOLT_LIGHT = (255, 223, 93)

def draw_icon():
    scale = 2
    W = SIZE * scale
    H = SIZE * scale
    img = Image.new("RGBA", (W, H), BG_COLOR + (255,))
    draw = ImageDraw.Draw(img)

    cx, cy = W // 2, H // 2
    r_rim = int(W * 0.44)

    # 1. 외곽 원형 림
    draw.ellipse(
        [cx - r_rim, cy - r_rim, cx + r_rim, cy + r_rim],
        fill=SHIELD_BG + (255,),
        outline=SHIELD_BORDER + (255,),
        width=int(14 * scale)
    )

    # 2. 방패(Shield) 폴리곤
    sw = int(W * 0.28)
    sh_top = int(H * 0.26)
    sh_mid = int(H * 0.52)
    sh_bot = int(H * 0.74)

    shield_pts = [
        (cx - sw, sh_top),
        (cx + sw, sh_top),
        (cx + sw, sh_mid),
        (cx, sh_bot),
        (cx - sw, sh_mid)
    ]
    draw.polygon(shield_pts, fill=(31, 111, 235, 60), outline=SHIELD_BORDER + (255,), width=int(10 * scale))

    # 3. 중앙 번개(Lightning Bolt) 폴리곤
    bolt_pts = [
        (cx + int(10 * scale), int(H * 0.32)),
        (cx - int(70 * scale), int(H * 0.52)),
        (cx - int(5 * scale), int(H * 0.52)),
        (cx - int(30 * scale), int(H * 0.70)),
        (cx + int(70 * scale), int(H * 0.48)),
        (cx + int(10 * scale), int(H * 0.48)),
    ]
    draw.polygon(bolt_pts, fill=BOLT_LIGHT + (255,), outline=BOLT_COLOR + (255,), width=int(4 * scale))

    # 리사이즈 및 저장
    img_final = img.resize((SIZE, SIZE), Image.Resampling.LANCZOS)
    img_final.save(OUT_DIR / "icon-512.png", "PNG")

    img_192 = img.resize((192, 192), Image.Resampling.LANCZOS)
    img_192.save(OUT_DIR / "icon-192.png", "PNG")

    img_180 = img.resize((180, 180), Image.Resampling.LANCZOS)
    img_180.save(OUT_DIR / "favicon-180.png", "PNG")

    img_32 = img.resize((32, 32), Image.Resampling.LANCZOS)
    img_32.save(OUT_DIR / "favicon-32.png", "PNG")

    print("[OK] 아이콘 생성 완료: 512, 192, 180, 32px")

if __name__ == "__main__":
    draw_icon()
