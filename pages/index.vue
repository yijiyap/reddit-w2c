<template>
    <div class="flex">
        <div class="mx-auto mt-10">
            <h1>Reddit W2C ft. r/FashionReps</h1>
        </div>
    </div>

    <div class="flex">
        <div class="mt-5 mx-auto">
            <p>Find reps easily</p>
        </div>
    </div>

    <div class="mt-10">
        <!-- on submit, pass the user_input to flask.py  -->
        <form action="" class="flex flex-col" @submit.prevent="handleSubmit">
            <div class="mx-auto">
                <input type="text" v-model="userInput" placeholder="Search for a product"
                    class="border-2 border-black rounded-lg ">
            </div>
            <div class="mx-auto">
                <button type="submit" class="border-2 border-black my-2" @click="handleSearch">Search</button>
            </div>
        </form>
        <div v-if="output">
            <p>Output: {{ output }}</p>
        </div>
    </div>
</template>

<script setup>
    // handle the user input and send to the backend on flask using $fetch
    import { ref } from "vue";
    const userInput = ref("");
    const output = ref("");

    async function handleSearch() {
        try {
            const response = await fetch("http://localhost:5000/api/process-data", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ data: userInput.value }),
            });
            const result = await response.json();
            output.value = result;
            console.log(result);
        } catch (error) {
            console.error(error);
        }
    }

</script>