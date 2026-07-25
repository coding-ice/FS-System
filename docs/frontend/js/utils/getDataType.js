function getDataType(value) {
  const type = Object.prototype.toString.call(value).slice(8, -1).toLowerCase();
  return type;
}
