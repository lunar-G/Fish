<template>
  <div class="sidebar-navigation hidde-sm hidden-xs">

    <div class="logo">
      <a href="#">淡水鱼 <em>养殖咨询平台</em></a>
    </div>
    <nav>
      <ul>
        <li style="color: wheat;font-size: 25px">用户名：{{ username }}</li>
        <li style="color: wheat;font-size: 25px">身份类型：用户</li>
      </ul>
    </nav>
  </div>


  <div class="page-content">
    <section id="blog" class="content-section">

      <section id="first-tab-group" style="margin-left: -150px" class="tabgroup">
        <b-row>
          <b-col lg="5"></b-col>

          <b-col lg="6">
            <b-row>
              <b-col lg="6">
                <label for="province" class="form-label">所在省份:</label>
                <input type="text" class="form-control" id="province" v-model="province" required>{{ province }}
              </b-col>
            </b-row>
            <b-row>
              <b-col lg="6">
                <label for="area" class="form-label">养殖面积:</label>
                <input type="text" class="form-control" id="area" v-model="area" required>
              </b-col>
            </b-row>
            <b-row>
              <b-col lg="6">
                <label for="species" class="form-label">养殖品种:</label>
                <input type="text" class="form-control" id="species" v-model="species" required>
              </b-col>
            </b-row>
            <b-row><br>
              <button class="btn btn-primary" style="font-size: 20px;width: 100px;margin-left: -300px" @click="subbmit">提交</button>
            </b-row>
          </b-col>

          <b-col lg="3"></b-col>
        </b-row>
      </section>


    </section>
  </div>
</template>
<script>
import axios from "axios";

export default {
  name: "PersonalInfo",
  data() {
    return {
      username: '',
      province: '',
      area: '',
      species: '',
      status: ''
    };
  },
  methods: {
    async subbmit() {
      const formData = new FormData();
      formData.append('username', this.username);
      formData.append('province', this.province);
      formData.append('area', this.area);
      formData.append('species', this.species);
      await axios
          .post('http://127.0.0.1:9999/PersonalInfo/', formData)
          .then(response => {
            this.status = response.data.data['status']
          }).catch(error => {
          })
      if (this.status === "ok") {
        this.$router.push({path: '/Recommend', query: {username: this.username}})
      }
    },

  },
  async mounted() {
    this.username = this.$route.query.username
    const formData = new FormData();
    formData.append('username', this.username);
    await axios
        .post('http://127.0.0.1:9999/PersonalInfo/', formData)
        .then(response => {
          this.status = response.data.data['status']
        }).catch(error => {
        })
    if (this.status === "ok") {
      this.$router.push({path: '/Recommend', query: {username: this.username}})
    }
  },
}
</script>
<style>


</style>