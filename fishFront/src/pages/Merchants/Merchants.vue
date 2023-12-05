<script>
import axios from "axios";

export default {
  name: "Merchants",
  data() {
    return {
      username: '',
      finished: [],
      toship: [],
      sale: [],
      forsale: [],
      stored: [],
    };
  },
  async mounted() {
    this.username = this.$route.query.username
    await this.refresh()
  },
  methods: {
    goBack() {
      this.$router.push({path: '/'})
    },
    async control(id, oper, type) {
      const formData = new FormData();
      formData.append('id', id);
      formData.append('oper', oper);
      formData.append('type', type);
      await axios
          .post('http://127.0.0.1:9999/ShopControl/', formData)
          .then(response => this.refresh()).catch(error => {
          })
    },
    async refresh() {
      const formData = new FormData();
      formData.append('username', this.username);
      await axios
          .post('http://127.0.0.1:9999/Merchant/', formData)
          .then(response => {
            this.sale = response.data.data['sale']
            this.forsale = response.data.data['forsale']
            this.stored = response.data.data['stored']
            this.finished = response.data.data['finished']
            this.toship = response.data.data['toship']
          }).catch(error => {
          })
    }
  },
  computed: {}
}
</script>

<template>
  <div class="sidebar-navigation hidde-sm hidden-xs">
    <div class="logo">
      <a href="#">淡水鱼 <em>养殖咨询平台</em></a>
    </div>
    <nav>
      <ul>
        <li style="color: wheat;font-size: 18px">用户名：{{ this.username }}</li>
        <li style="color: wheat;font-size: 18px">身份类型：商家</li>
        <li style="color: wheat;font-size: 18px" id="leave" @click="goBack">退出登录</li>
      </ul>
    </nav>
  </div>
  <div class="page-content">
    <section id="blog" class="content-section">
      <div class="section-content">
        <div class="tabs-content">
          <div class="wrapper">
            <ul class="tabs clearfix" data-tabgroup="first-tab-group">
              <li><a href="#tab1" class="active">商品管理</a></li>
              <li><a href="#tab2">订单管理</a></li>
            </ul>
            <section id="first-tab-group" class="tabgroup">
              <div id="tab1">
                <table class="table table-bordered border-primary">
                  <thead>
                  <tr style="font-size: 20px;height: 30px">
                    <th>商品id</th>
                    <th>商品名</th>
                    <th>价格</th>
                    <th>状态</th>
                    <th>操作</th>
                  </tr>
                  </thead>

                  <tbody style="font-size: 15px">

                  <tr v-for="mer in sale" :key="mer.id">
                    <td> {{ mer.id }}</td>
                    <td>{{ mer.name }}</td>
                    <td>{{ mer.price }}</td>
                    <td>{{ mer.status }}</td>
                    <td>
                      <button type="button" class="btn btn-outline-success" style="font-size: 15px;height: 30px" @click="control(mer.id , '下架', '商品')">下架</button>
                    </td>
                  </tr>

                  <tr v-for="mer in forsale" :key="mer.id">
                    <td> {{ mer.id }}</td>
                    <td>{{ mer.name }}</td>
                    <td>{{ mer.price }}</td>
                    <td>{{ mer.status }}</td>
                    <td>
                      <button type="button" class="btn btn-outline-danger" style="font-size: 15px;height: 30px" @click="control(mer.id , '撤销', '商品')">撤销</button>
                    </td>
                  </tr>

                  <tr v-for="mer in stored" :key="mer.id">
                    <td> {{ mer.id }}</td>
                    <td>{{ mer.name }}</td>
                    <td>{{ mer.price }}</td>
                    <td>{{ mer.status }}</td>
                    <td>
                      <button type="button" class="btn btn-outline-primary" style="font-size: 15px;height: 30px" @click="control(mer.id , '上架', '商品')">上架</button>
                    </td>
                  </tr>
                  </tbody>
                </table>
              </div>

              <div id="tab2">
                <table class="table table-bordered border-primary">
                  <thead>
                  <tr style="font-size: 20px;height: 30px">
                    <th>订单ID</th>
                    <th>商品</th>
                    <th>数量</th>
                    <th>总价</th>
                    <th>收货人</th>
                    <th>收货地址</th>
                    <th>订单状态</th>
                    <th>操作</th>
                  </tr>
                  </thead>

                  <tbody style="font-size: 15px">

                  <tr v-for="mer in toship" :key="mer.id">
                    <td> {{ mer.id }}</td>
                    <td>{{ mer.item }}</td>
                    <td>{{ mer.number }}</td>
                    <td>{{ mer.price }}</td>
                    <td>{{ mer.consignee }}</td>
                    <td>{{ mer.address }}</td>
                    <td>{{ mer.status }}</td>
                    <td>
                      <button type="button" class="btn btn-outline-primary" style="font-size: 15px;height: 30px" @click="control(mer.id , '发货', '订单')">发货</button>
                    </td>
                  </tr>


                  <tr v-for="mer in finished" :key="mer.id">
                    <td> {{ mer.id }}</td>
                    <td>{{ mer.item }}</td>
                    <td>{{ mer.number }}</td>
                    <td>{{ mer.price }}</td>
                    <td>{{ mer.consignee }}</td>
                    <td>{{ mer.address }}</td>
                    <td>{{ mer.status }}</td>
                    <td>
                      <button type="button" class="btn btn-outline-danger" style="font-size: 15px;height: 30px" @click="control(mer.id , '删除', '订单')">删除</button>
                    </td>
                  </tr>
                  </tbody>
                </table>

              </div>
            </section>

          </div>
        </div>
      </div>

    </section>


  </div>
</template>

<style>
@import '/src/assets/css/bootstrap.css';
@import '/src/assets/css/bootstrap-theme.min.css';
@import '/src/assets/css/owl-carousel.css';
@import '/src/assets/css/templatemo-style.css';
@import '/src/assets/css/bot5.css';

.scroll-box {
  background-color: #fff;
  border: 1px solid #ccc;
  border-radius: 5px;
  padding: 10px;
  height: 14vh;
  overflow-y: scroll;
}

.info-box {
  font-size: 15px;
  width: 300px;
  padding: 15px;
  text-align: left;
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
}
</style>