<script>
import axios from "axios";

export default {
  name: 'Home',
  data() {
    return {
      username: '',
      password: '',
      status: '',
      identity: ''
    };
  },
  methods: {
    async login() {
      const formData = new FormData();
      formData.append('username', this.username);
      formData.append('password', this.password);
      await axios
          .post('http://127.0.0.1:9999/Login/', formData)
          .then(response => (
              this.status = response.data.data['status']))
          .catch(error => {
          });
      if (this.status === "user") {
        this.$router.push({path: '/PersonalInfo', query: {username: this.username}});
      } else if (this.status === "shops") {
        this.$router.push({path: '/Merchants', query: {username: this.username}});
      } else if (this.status === "admin") {
        this.$router.push({path: '/Administrator', query: {username: this.username}});
      }
    },
    register() {
      // this.$router.pop({path: '/',});
      this.$router.push('/Register')
    }
  },
  computed: {},
};
</script>
<template>
  <div class="container">
    <video autoplay="autoplay" loop muted preload class="video">
      <source src="/src/assets/image/home.mp4">
    </video>
    <div class="loginDiv">
      <div id="form">
        <label>账号：<input type="text" v-model="this.username"></label><br><br>
        <label>密码：<input type="password" v-model="this.password"></label>
        <div class="inputDiv">
          <input type="submit" class="button" value="登录" @click="login">
          &nbsp
          <input type="button" class="button" value="注册" @click="register">
        </div>
        <br>
      </div>
    </div>
  </div>
</template>
<style>
.container {
  position: absolute;
  width: 100%;
  height: 707px;
}

label {
  font-size: 20px;
}

.video {
  position: absolute;
  object-fit: fill;
  z-index: 1;
  width: 1520px;
  height: 100%;
}

.loginDiv {
  width: 27%;
  position: absolute;
  top: 180px;
  left: 550px;
  z-index: 2;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 300px;
  background-color: rgba(75, 81, 95, 0.3);
  box-shadow: 7px 7px 17px rgba(52, 56, 66, 0.5);
  border-radius: 5px;
}

input {
  margin-left: 15px;
  border-radius: 5px;
  border-style: hidden;
  height: 30px;
  width: 200px;
  background-color: rgba(216, 191, 216, 0.5);
  outline: none;
  color: #f0edf3;
  padding-left: 10px;
}

.inputDiv {
  font-size: 20px;
  text-align: center;
  margin-top: 30px;
}

.button {
  border-color: cornsilk;
  background-color: rgba(100, 149, 237, .7);
  color: aliceblue;
  border-style: hidden;
  border-radius: 5px;
  width: 100px;
  height: 31px;
  font-size: 16px;
}
</style>