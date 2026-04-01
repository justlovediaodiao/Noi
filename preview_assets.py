#!/usr/bin/env python3
"""
预览 Noi App 的图标
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches

# ic_launcher_foreground.xml - 108x108 viewport
# 背景: M0,0 h108 v108 h-108 z
# 横线1: M30,34 h48 v8 h-48 z
# 横线2: M30,50 h48 v8 h-48 z
# 横线3: M30,66 h32 v8 h-32 z

def draw_launcher_icon(ax):
    """绘制启动图标 - 绿色背景 + 三条白线"""
    ax.set_xlim(0, 108)
    ax.set_ylim(108, 0)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('ic_launcher_foreground', fontsize=12)

    # 背景 #5B9A8B
    bg = patches.Rectangle((0, 0), 108, 108, facecolor='#5B9A8B', edgecolor='none')
    ax.add_patch(bg)

    # 三条白色横线
    # 线1: 30,34 宽48 高8
    line1 = patches.Rectangle((30, 34), 48, 8, facecolor='white', edgecolor='none')
    ax.add_patch(line1)

    # 线2: 30,50
    line2 = patches.Rectangle((30, 50), 48, 8, facecolor='white', edgecolor='none')
    ax.add_patch(line2)

    # 线3: 30,66 宽32
    line3 = patches.Rectangle((30, 66), 32, 8, facecolor='white', edgecolor='none')
    ax.add_patch(line3)


def draw_notification_icon(ax):
    """绘制通知图标 - 文档形状"""
    ax.set_xlim(0, 24)
    ax.set_ylim(24, 0)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('ic_notification', fontsize=12)

    # 外框形状 - 文档轮廓
    # pathData: M19,3 H5 C3.89,3 3,3.89 3,5 V19 C3,20.11 3.89,21 5,21 H19 C20.11,21 21,20.11 21,19 V5 C21,3.89 20.11,3 19,3
    # 简化为矩形
    doc = patches.FancyBboxPatch((3, 3), 18, 18, boxstyle="round,pad=0,rounding_size=1",
                                  facecolor='#5B9A8B', edgecolor='#5B9A8B', linewidth=2)
    ax.add_patch(doc)

    # 两条横线
    # 线1: M17,13 H7 V11 H17 V13  -> y=11, 高2, 从x=7到x=17
    line1 = patches.Rectangle((7, 11), 10, 2, facecolor='white', edgecolor='none')
    ax.add_patch(line1)

    # 线2: M17,9 H7 V7 H17 V9  -> y=7, 高2
    line2 = patches.Rectangle((7, 7), 10, 2, facecolor='white', edgecolor='none')
    ax.add_patch(line2)


# 创建图形
fig, axes = plt.subplots(1, 2, figsize=(8, 4))

draw_launcher_icon(axes[0])
draw_notification_icon(axes[1])

plt.suptitle('Noi App - Icon Preview', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()
