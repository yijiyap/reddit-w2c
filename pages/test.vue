<template>
  <div>
    <input v-model="inputData" type="text" placeholder="Enter your data" />
    <button @click="sendData">Submit</button>
  </div>
  <div v-if="output">
    {{ output }}
  </div>
</template>

<script setup>
import { ref } from 'vue';

const inputData = ref('');
const output = ref('');

async function sendData() {
  try {
    const response = await fetch('http://localhost:5000/api/process-data', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ data: inputData.value }),
    });
    const result = await response.json();
    output.value = result;
    console.log(result);
  } catch (error) {
    console.error(error);
  }
}

</script>