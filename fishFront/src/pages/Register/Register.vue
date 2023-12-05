<script>
import axios from "axios";

export default {
  name: 'Register',
  data() {
    return {
      username: '',
      password: '',
      repassword: '',
      identity: '',
      status: '',
      isSame: 0,
      telephone: ''
    };
  },
  methods: {
    async register() {
      const formData = new FormData();
      formData.append('username', this.username);
      formData.append('password', this.password);
      formData.append('identity', this.identity);
      formData.append('telephone', this.telephone);
      if (this.password === this.repassword) {
        await axios
            .post('http://127.0.0.1:9999/Register/', formData)
            .then(response => (
                this.status = response.data.data['status']))
            .catch(error => {
            });
      }
      if (this.status === 'ok') {
        alert('注册成功')
        this.$router.go(-1)
      }
    },
    goBack() {
      this.$router.go(-1)
    }
  },
  computed: {
    check() {
      if (this.password !== '') {
        if (this.password === this.repassword) {
          this.isSame = 0
        } else
          this.isSame = 1
      }

    }
  }
};
</script>
<template>
  <div class="container">
    <video autoplay="autoplay" loop muted preload class="video">
      <source src="/src/assets/image/home.mp4">
    </video>
    <div class="loginDiv">
      <div id="form">
        <label>账号<input type="text" v-model="this.username"></label><br>
        <label>密码<input type="password" v-model="this.password" @change="check"></label><br>
        <label>确认密码<input type="password" v-model="this.repassword" @change="check"></label><br>
        <label>手机号码<input type="text" v-model="this.telephone" @change="check"></label>
        <div style="margin-top: -10px">
          <label>身份类型</label>
          <select v-model="identity" style="font-size: 18px;margin-left: 20px;margin-top: 10px">
            <option selected>用户</option>
            <option>商家</option>
          </select>

        </div>

        <div v-if="isSame">6666</div>
        <div class="inputDiv">
          <input type="submit" class="button" @click="goBack" value="返回">
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

.radio-buttons input[type="radio"],
.radio-buttons label {
  display: inline-block;
  margin-right: 10px; /* 可以调整单选框和标签之间的间距 */
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