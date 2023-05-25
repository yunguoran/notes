# 代码整洁之道

## 序

- 宏大建筑中最细小的部分，比如关不紧的门、有点没铺平的地板，甚至是凌乱的桌面，都会将整个大局的魅力毁灭殆尽。
- 对于代码，应无情地做重构。
- 写出可读的代码，重要程度不亚于写出可执行的代码。
- 你当用为自己第一个孩子命名般的谨慎来给变量命名。

## 第一章 整洁代码

- 将需求明确到机器可以执行的细节程度，就是编程要做的事。
- 勒布朗（LeBlanc）法则：稍后等于永不（Later equals never）。
- 花时间保持代码整洁不但有关效率，还有关生存。

## 第二章 有意义的命名

选个好名字要花时间，但省下来的时间比花掉的多。注意命名，而且一旦发现有更好的名称，就换掉旧的。

```java
public List<int[]> getFlaggedCells() {
  List<int[]> flaggedCells = new ArrayList<int[]>();
  for (int[] cell : gameBoard)
  if (cell[STATUS_VALUE] == FLAGGED)
    flaggedCells.add(cell);
  return flaggedCells;
}

// 不用 int 数组表示单元格，而是另写一个类。该类包括一个名副其实的函数（称为 isFlagged），从而掩盖住那个 Magic Value。
public List<Cell> getFlaggedCells() {
  List<Cell> flaggedCells = new ArrayList<Cell>();
  for (Cell cell : gameBoard)
    if (cell.isFlagged())
      flaggedCells.add(cell);
  return flaggedCells;
}
```

- 不要使用小写字母 l 和大写字母 O。
- 假设你有一个 Product 类。如果还有一个 ProductInfo 或 ProductData 类，那它们的名称虽然不同，意思却无区别。Info 和 Data 就像 a、an 和 the 一样，是意义含混的废话。
- 类和对象名应该是名词和名词短语。
- 方法名应当是动词或动词短语。
