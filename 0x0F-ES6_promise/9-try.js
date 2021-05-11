export default function guardrail(mathFunction) {
  const queue = [];
  try {
    const val = mathFunction();
    queue.push(val);
  } catch (error) {
    queue.push(error.toString().substring(0, 25));
  } finally {
    queue.push('Guardrail was processed');
  }
  return queue;
}
