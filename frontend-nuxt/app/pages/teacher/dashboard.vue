<template>
  <v-container class="fill-height" fluid>
    <v-row align="center" justify="center">
      <v-col cols="12" md="8">
        <v-card>
          <v-card-title>Teacher Dashboard</v-card-title>
          <v-card-text>
            <v-alert type="info">Teacher dashboard page placeholder</v-alert>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <h1>Teacher Dashboard</h1>
        <p v-if="userName">Welcome, {{ userName }}!</p>
        <p v-if="userRole">Role: {{ userRole }}</p>
        <p v-if="userId">User ID: {{ userId }}</p>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
const userName = ref('')
const userRole = ref('')
const userId = ref('')

onMounted(() => {
  userName.value = localStorage.getItem('userName') || ''
  userRole.value = localStorage.getItem('userRole') || ''
  userId.value = localStorage.getItem('userId') || ''
})
</script>

<style scoped>
/* ...existing styles... */
</style>
