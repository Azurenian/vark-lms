<template>
  <v-container fluid class="fill-height">
    <v-row align="center" justify="center">
      <v-col cols="12" sm="8" md="6">
        <v-card class="pa-8 text-center">
          <v-card-title class="text-h5 mb-4">
            Authenticating via LTI
          </v-card-title>
          <v-progress-circular
            indeterminate
            color="primary"
            size="64"
            class="mb-4"
          />
          <v-card-text>
            <p class="text-body-1">Please wait while we log you in...</p>
            <p v-if="error" class="text-error mt-2">{{ error }}</p>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
const route = useRoute()
const router = useRouter()
const error = ref('')

onMounted(() => {
  const userId = route.query.user_id
  const name = route.query.name
  const email = route.query.email
  const role = route.query.role
  const redirect = route.query.redirect

  if (userId && role && redirect) {
    try {
      // Store user info in localStorage for API calls
      localStorage.setItem('userId', userId)
      localStorage.setItem('userName', name || '')
      localStorage.setItem('userEmail', email || '')
      localStorage.setItem('userRole', role)

      // Redirect to the dashboard provided by backend
      router.push(redirect)
    } catch (err) {
      error.value = 'Failed to authenticate. Please try again.'
      console.error('LTI Authentication error:', err)
    }
  } else {
    error.value = 'Invalid authentication data received.'
    setTimeout(() => {
      router.push('/')
    }, 3000)
  }
})
</script>
