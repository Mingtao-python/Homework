# 第18周：Logistic Regression 解释题（5 题）
### 深入版
## 1. Logistic 如何做分类？
Logistic Regression 会对输入特征做线性组合：
z = wx + b  
然后通过 sigmoid 或 softmax 将结果转换成概率。  
概率最高的类别就是最终输出。  
它本质上学习了一条线性决策边界，根据特征把样本推向不同类别。

---

## 2. 哪个特征最重要？
根据模型的 coef_（权重）绝对值平均值：

- Length：0.104 
- MathWords：0.535
- CodingWords：0.618  

权重越大说明特征越重要，因此最重要的特征是 **CodingWords（Coding 关键词数量）**。

---

## 3. 删除特征后发生什么？
特征消融实验结果：

- 删除 Length → Accuracy = 1.0（无影响甚至更好）
- 删除 MathWords → Accuracy = 0.66（性能下降）
- 删除 CodingWords → Accuracy = 0.66（性能下降最大）

删除最重要特征（CodingWords）后模型性能明显下降，说明它对分类贡献最大。

---

## 4. 输入边界在哪里？
输入边界在 **Validator → Feature Extractor 之间**。  
只有通过 Validator 的输入才会进入模型。  
Validator 会检查：

- 空输入  
- 超长输入  
- 非 ASCII 比例  
- 重复词 spam  

这些规则共同构成系统的执行边界。

---

## 5. 如何防御绕过？
可以通过以下方式增强防御：

- 多特征联合判断（长度 + 乱码 + 重复词）  
- 更严格的阈值  
- 关键词黑名单  
- 对边界附近输入进行二次验证  
- 日志监控可疑输入  

这样可以阻止攻击者构造“边界附近”的输入绕过系统，提高整体安全性。