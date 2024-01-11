export default function createInt8TypedArray9(length, position, value) {
  const buffer = new ArrayBuffer(length);
  const view = new Int8Array(buffer);
  if (position < 0 || position >= length) {
    throw TypeError('Position is outside of range');
  }
  view[position] = value;
  return buffer;
}
