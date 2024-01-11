export default function guardrail(mathFunction) {
  const queue = [];
  try {
    queue.push(mathFunction());
  } catch (element) {
    queue.push('Error: '.concat(element.message));
  } finally {
    queue.push('Guardrail was processed');
  }
  return queue;
}
