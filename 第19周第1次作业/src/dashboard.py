from pathlib import Path

def build_dashboard_html():
    dashboard_data = {
        "question_count": 8,
        "category_stats": {"Math": 4, "Coding": 4},
        "accuracy": 0.875,
        "error_analysis": ["Question 3: wrong category", "Question 6: wrong answer"],
    }

    html = f"""<!DOCTYPE html>
<html lang=\"en\">
<head>
    <meta charset=\"UTF-8\">
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
    <title>AI Learning Analytics Dashboard</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 24px; }}
        .card {{ border: 1px solid #ddd; padding: 16px; margin-bottom: 16px; border-radius: 8px; }}
        button {{ padding: 8px 14px; margin-right: 8px; }}
    </style>
</head>
<body>
    <h1>AI Learning Analytics Dashboard</h1>
    <div class=\"card\">
        <h2>Question Statistics</h2>
        <p id=\"questionCount\">Total questions: {dashboard_data['question_count']}</p>
    </div>
    <div class=\"card\">
        <h2>Category Statistics</h2>
        <p id=\"categoryStats\">Math: {dashboard_data['category_stats']['Math']} | Coding: {dashboard_data['category_stats']['Coding']}</p>
    </div>
    <div class=\"card\">
        <h2>Accuracy</h2>
        <p id=\"accuracyText\">Accuracy: {dashboard_data['accuracy']:.2%}</p>
    </div>
    <div class=\"card\">
        <h2>Error Analysis</h2>
        <ul id=\"errorList\">
            <li>{dashboard_data['error_analysis'][0]}</li>
            <li>{dashboard_data['error_analysis'][1]}</li>
        </ul>
    </div>

    <button id=\"showBtn\">Show Result</button>
    <button id=\"hideBtn\">Hide Result</button>
    <button id=\"reloadBtn\">Reload</button>

    <div id=\"resultPanel\" class=\"card\" style=\"display:none;\">
        <h2>Dynamic Result</h2>
        <p id=\"dynamicMessage\">This panel is controlled by JavaScript.</p>
    </div>

    <script>
        const resultPanel = document.getElementById("resultPanel");
        const dynamicMessage = document.getElementById("dynamicMessage");

        document.getElementById("showBtn").onclick = function() {{
            resultPanel.style.display = "block";
            dynamicMessage.innerHTML = "Hello";
        }};

        document.getElementById("hideBtn").onclick = function() {{
            resultPanel.style.display = "none";
        }};

        document.getElementById("reloadBtn").onclick = function() {{
            window.location.reload();
        }};
    </script>
</body>
</html>
"""

    output_path = Path(__file__).resolve().parents[1] / "week19_dashboard.html"
    output_path.write_text(html, encoding="utf-8")
    print(f"3. 已生成前端页面: {output_path}")
    print("   页面内使用了 document.getElementById() 和 button.onclick 实现动态显示、隐藏和重新加载。")
    print()
