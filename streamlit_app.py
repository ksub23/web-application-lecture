import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# 1. 웹 페이지 기본 설정
st.set_page_config(page_title="삼각함수 그래프 탐구기", layout="wide")
st.title("📊 y = a sin(bx + c) 그래프 탐구 애플리케이션")
st.write("슬라이더를 조절하며 삼각함수의 변형 규칙을 스스로 발견해 보세요!")

# 화면을 두 칸으로 분할 (왼쪽: 조작 및 설명 / 오른쪽: 그래프 차트)
col1, col2 = st.columns([1, 1.5])

with col1:
    st.subheader("🎛️ 파라미터 조작 패널")

    a = st.slider("계수 a (최대/최소 제어)", min_value=-4.0, max_value=4.0, value=1.0, step=0.5)
    b = st.slider("계수 b (주기 제어)", min_value=0.5, max_value=4.0, value=1.0, step=0.5)
    c = st.slider("계수 c (평행이동 관여)", min_value=-3.14, max_value=3.14, value=0.0, step=0.1)

    st.markdown("---")

    show_hint = st.checkbox("💡 x축 평행이동량 공식 힌트 보기 (b로 묶기)")
    if show_hint:
        shift = -c / b
        st.info(
            f"👉 y = {a} sin({b}(x + {c / b:.2f})) 형태로 변형됩니다. "
            f"따라서 x축 방향 평행이동량은 {shift:.2f}입니다."
        )

    st.markdown("---")
    st.subheader("🎯 퀴즈 미션 모드")
    quiz_on = st.checkbox("퀴즈 도전하기")
    if quiz_on:
        st.warning("🔥 **미션 목표**: 최댓값 = 2, 주기 = $\\pi$, x축 평행이동 = 0 인 그래프를 만드세요!")
        if a == 2.0 and b == 2.0 and c == 0.0:
            st.balloons()
            st.success("🎉 정답입니다! 미션을 성공하셨습니다!")

with col2:
    st.subheader("📈 실시간 그래프 시각화")

    x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)

    y_base = np.sin(x)
    y_transform = a * np.sin(b * x + c)

    fig, ax = plt.subplots(figsize=(8, 5))

    ax.axhline(0, color="black", linewidth=1.2)
    ax.axvline(0, color="black", linewidth=1.2)
    ax.grid(True, linestyle="--", alpha=0.6)

    ax.plot(x, y_base, label="y = sin(x) [basic form]", color="gray", linestyle="--", alpha=0.7)
    ax.plot(x, y_transform, label=f"y = {a}*sin({b}x + {c})", color="#1E88E5", linewidth=2.5)

    ax.set_xticks([-2 * np.pi, -np.pi, 0, np.pi, 2 * np.pi])
    ax.set_xticklabels(["$-2\\pi$", "$-\\pi$", "0", "$\\pi$", "$2\\pi$"])

    ax.set_ylim(-4.5, 4.5)
    ax.legend(loc="upper right")

    st.pyplot(fig)

    st.subheader("📝 현재 그래프의 성질 정리")
    st.write(f"• **최댓값**: {abs(a)}  |  **최솟값**: {-abs(a)}")
    st.write(f"• **주기**: $2\\pi / {b}$ = **{2 * np.pi / b:.2f}**")
