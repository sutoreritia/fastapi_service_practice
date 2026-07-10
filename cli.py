from app.agent.agent_service import run_agent


def main():
    print("=== 中央廚房企劃 AI 助理 ===")
    print("輸入 exit 結束。範例：請幫我查 K1001 配送狀態")

    while True:
        task = input("\n任務> ").strip()

        if task.lower() in ["exit", "quit", "q"]:
            print("已結束。")
            break

        if not task:
            continue

        result = run_agent(task)
        print(f"[大腦選工具]: {result['plan']['selected_tool']}")
        print(f"[大腦判斷理由]: {result['plan']['reason']}")
        print(f"[最終回答]: {result['final_answer']}")


if __name__ == "__main__":
    main()