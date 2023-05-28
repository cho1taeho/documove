<template>
  <div>
    <input type="text" class="input-box" placeholder="댓글 내용" v-model="commentItem.content">
    <button class="btn btn-create" @click="createComment">댓글 작성</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'CommentForm',
  props: {
    review: {
      type: Object,
      required: true,
    }
  },
  data() {
    return {
      commentItem: {
        content: null,
      }
    }
  },
  methods: {
    setToken() {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
     createComment() {
      const movieId = this.movie && this.movie.id; // 영화 ID
      if (!movieId) {
        console.error('영화 ID가 없습니다.');
        return;
      }
      const commentItemSet = {
        commentItem: this.commentItem,
        token: this.setToken(),
      };
      axios({
        method: 'POST',
        url: `http://127.0.0.1:8000/community/reviews/comments/`,
        data: commentItemSet.commentItem,
        headers: commentItemSet.token,
      })
        .then((response) => {
          // 댓글 작성 성공 시 처리할 로직
          console.log('댓글 작성 성공:', response.data);
        })
        .catch((error) => {
          // 댓글 작성 실패 시 처리할 로직
          console.error('댓글 작성 실패:', error);
        });
      this.commentItem.content = null;
    },
  },
}
</script>

<style>

</style>
