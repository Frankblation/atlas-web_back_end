export default function appendToEachArrayValue(array, appendString) {
  const newArray = [];
  for (const string of array) {
    newArray.push(appendString + string);
  }

  return newArray;
}
