<template>
  <div class="giving-detail" v-if="giving">
    <div class="container">
      <div class="row">
        <div class="col">
          <br>
          <h1>{{ giving.title }}</h1>
          <p><strong>Active:</strong> {{ giving.active }}</p>
          <p><strong>Summary:</strong> {{ giving.summary }}</p>
          <p><strong>Theme name:</strong> {{giving.themeName}} </p>
          <p><strong>Country :</strong> {{giving.country}} </p>
          <p><strong>Region :</strong> {{giving.region}} </p>
          <p><strong>Activites :</strong> {{giving.activities}} </p>
          

          <img :src="giving.imageLink" alt="Giving Image" class="img-fluid">
        </div>
      </div>
      <button @click="givingPoint()" >후원하기</button>
    </div>
  </div>
  <div v-else>Loading...</div>
</template>


<script>
import axios from "axios"

export default {
  
  data() {
    return {
      giving: null,
    };
  },
  async created() {
    const giving_id = this.$route.query.giving_id
    if (giving_id) {
      try {
        const response = await axios.get(`http://127.0.0.1:8000/movies/giving`)
        this.giving = response.data.find(giving => giving.id === giving_id)
      } catch(error) {
        console.error(error)
      }
    }    
  },
  methods: {
    async givingPoint(){
      const givingId = this.giving.id
      const point = prompt("how much?")
      let points
      try {
        const whoIAm = await axios.get(`http://127.0.0.1:8000/accounts/mypage/`).then(res => res.data);
        points = whoIAm.user.points
        await axios.post(`http://127.0.0.1:8000/accounts/giving/`,
        {
          username : whoIAm.user.username,
          password : whoIAm.user.password,
          point : parseInt(point),
          givingId : givingId
        })
        alert('후원성공했습니다 \n현재 남은 포인트 : ' + (whoIAm.user.points - point))
      } catch(err){
        alert('포인트가 부족합니다. \n현재 남은 포인트 : ' + points)
      }
    
    },
    getOriginalImageLink() {
       if (this.giving && this.giving.imageLink && this.giving.imageLink.length > 0) {
        const imageLinkArray = Array.from(this.giving.imageLink); 
        const originalImage = imageLinkArray.find(link => link.size === 'original');
        if (originalImage) {
          return originalImage.link;
        }
      }
      return '' 
    }
  }
}
</script>

<style scoped>
.img-fluid {
  width: 50%;
  max-height: 500px;
  object-fit: cover;
}

</style>
