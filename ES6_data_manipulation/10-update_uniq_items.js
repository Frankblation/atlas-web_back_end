export default function updateUniqueItems(newMap) {
  if (!(newMap instanceof Map)) {
    throw new Error('Cannot process');
  }
  newMap.forEach((key, value) => {
    if (key === 1) {
      newMap.set(value, 100);
    }
  });
  return newMap;
}
