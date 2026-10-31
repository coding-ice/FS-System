function dot(left: number[], right: number[]): number {
  return left.reduce((sum, value, index) => sum + value * right[index], 0);
}

function softmax(row: number[]): number[] {
  const peak = Math.max(...row);
  // 先减去最大值，避免指数太大溢出；不改变这一行的相对关系。
  const lifted = row.map((value) => Math.exp(value - peak));
  const total = lifted.reduce((sum, value) => sum + value, 0);
  return lifted.map((value) => value / total);
}

// 计算 Attention(Q, K, V) = softmax(QK^T / sqrt(d_k)) V。
// 这里令 Q、K、V 都等于 vectors，相当于三组投影矩阵都是单位矩阵。
function scaledDotProductAttention(vectors: number[][]): {
  weights: number[][];
  outputs: number[][];
} {
  const width = vectors[0].length;
  const scale = Math.sqrt(width);
  const weights = vectors.map((query) =>
    softmax(vectors.map((key) => dot(query, key) / scale)),
  );

  const outputs = weights.map((row) => {
    const mixed = Array.from({ length: width }, () => 0);
    row.forEach((weight, valueIndex) => {
      vectors[valueIndex].forEach((component, index) => {
        mixed[index] += weight * component;
      });
    });
    return mixed;
  });

  return { weights, outputs };
}

const tokens = ["猫", "追", "鼠"];
// 手写向量只为演示：“猫”和“鼠”更接近，“追”几乎与它们正交。
const vectors = [
  [1, 0],
  [0, 1],
  [1, 0.2],
];

const { weights, outputs } = scaledDotProductAttention(vectors);

console.log("每一行是该 token 分给所有 token 的注意力权重，行和为 1：");
tokens.forEach((token, index) => {
  const pairs = tokens
    .map((name, nameIndex) => `${name}:${weights[index][nameIndex].toFixed(3)}`)
    .join("  ");
  console.log(`${token} -> ${pairs}`);
});

console.log("加权求和后的新表示：");
tokens.forEach((token, index) => {
  const rendered = outputs[index].map((component) => component.toFixed(3)).join(", ");
  console.log(`${token} -> [${rendered}]`);
});
