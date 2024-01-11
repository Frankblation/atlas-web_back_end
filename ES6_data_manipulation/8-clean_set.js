export default function cleanSet(set, startString) {
  const filterValues = Array.from(set).filter((value) => value.startsWith(startString));
  const endString = filterValues.join('-');
  return endString;
}
