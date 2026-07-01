def security_boundary_analysis():
    print("4. 安全模块：执行边界分析")
    allowed_examples = [
        "Explain Python loops",
        "Solve 2 + 2",
        "What is the difference between precision and recall?",
    ]
    blocked_examples = [
        "__import__('os').system('rm -rf /')",
        "<script>alert('xss')</script>",
        "eval('1+1')",
        "; DROP TABLE users;",
    ]

    print("   允许执行的输入：")
    for example in allowed_examples:
        print(f"   - {example}")
    print("   禁止执行的输入：")
    for example in blocked_examples:
        print(f"   - {example}")
    print("   结论：仅接受简短、可解释、非代码执行的自然语言输入；拒绝包含脚本、命令、SQL、eval、import等危险模式的内容。")
    print()
