<template>
  <v-container fluid>
    <v-row>
      <v-col cols="12">
        <v-card>
          <v-card-title>
            Top Donator
          </v-card-title>
          <v-card-text>
            <v-row>
              <v-col cols="4">
                <h3>{{ topDonator.username }}</h3>
              </v-col>
              <v-col cols="4">
                <h3>Total Donation: {{ topDonator.total_donation }}</h3>
              </v-col>
              <v-col cols="4">
                <h3>User Count: {{ topDonator.user_count }}</h3>
              </v-col>
            </v-row>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: 'DonationCard',
  props: {
    topDonator: {
      type: Object,
      required: true
    }
  }
}
</script>

<style scoped>
/* 필요한 스타일을 추가해주세요 */
</style>