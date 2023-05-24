// <template>
  <div>
    <br>
    <h2>{{ selectedTheme }} Giving</h2>
    <div class="card-deck">
      <div v-for="giving in themeGivings" :key="giving.id" class="card">
        <img :src="giving.image" class="card-img-top" alt="Giving Image">
        <div class="card-body">
          <h5 class="card-title">{{ giving.title }}</h5>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex'

export default {
  name: 'GivingTheme',
  computed: {
    ...mapState(['givings', 'selectedTheme']),
    // ...mapGetters(['themeGivings']),
    themeGivings() {
      return this.givings.filter(giving => giving.theme.includes(this.theme))
    },
    theme() {
      return this.$route.params.theme
    },

  },
  methods: {
    ...mapActions(['getGivings'])
  },
  created() {
    this.getGivings()
  }
}
</script>

<style>
.card {
  margin-bottom: 20px;
}
</style>
