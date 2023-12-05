<template>
  <div class="sidebar-navigation hidde-sm hidden-xs">

    <div class="logo">
      <a href="#">淡水鱼 <em>养殖咨询平台</em></a>
    </div>
    <nav>
      <ul>
        <li style="color: wheat;font-size: 25px">用户名：admin</li>
        <li style="color: wheat;font-size: 25px">身份类型：管理员</li>
        <li style="color: wheat;font-size: 25px" id="leave" @click="goBack">退出登录</li>
      </ul>
    </nav>
  </div>


  <div class="page-content">
    <section id="blog" class="content-section">

      <ul class="tabs clearfix" data-tabgroup="first-tab-group">
        <li><a href="#tab1" class="active">信息管理</a></li>
        <li><a href="#tab2" class="active">账号管理</a></li>
        <li><a href="#tab3" class="active">商品审核</a></li>
        <li><a href="#tab4" class="active">消息回复</a></li>
      </ul>

      <section id="first-tab-group" class="tabgroup">
        <div id="tab1" class=scrollable-div>
          <div class="kp">
            名称：
            <div style="display: inline"> 青鱼</div>
            <br>
            详细页网址：
            <a style="display: inline" href=" https://baike.baidu.com/item/%E9%9D%92%E9%B1%BC/680135">https://baike.baidu.com/item/%E9%9D%92%E9%B1%BC/680135</a>
            <br>
            状态：
            <div style="display: inline"> 已通过</div>
            <br>
            操作：
            <button type="button" class="btn btn-outline-danger" style="font-size: 15px" @click="infoDelete(name)">删除</button>
          </div>
          <br>
          <div class="kp">
            名称：
            <div style="display: inline"> 鲫鱼</div>
            <br>
            详细页网址：
            <a style="display: inline" href="https://baike.baidu.com/item/%E9%B2%AB/679608?fromtitle=%E9%B2%AB%E9%B1%BC&froid=322414">https://baike.baidu.com/item/%E9%B2%AB/679608?fromtitle=%E9%B2%AB%E9%B1%BC&froid=322414</a>
            <br>
            状态：
            <div style="display: inline"> 已通过</div>
            <br>
            操作：
            <button type="button" class="btn btn-outline-danger" style="font-size: 15px" @click="infoDelete(name)">删除</button>
          </div>

          <br>
          <div class="kp">
            名称：
            <div style="display: inline"> 鲢鱼</div>
            <br>
            详细页网址：
            <a style="display: inline" href="https://baike.baidu.com/item/%E9%B2%87/466538?fromtitle=%E9%B2%B6%E9%B1%BC&froid=1579868">https://baike.baidu.com/item/%E9%B2%87/466538?fromtitle=%E9%B2%B6%E9%B1%BC&froid=1579868</a>
            <br>
            状态：
            <div style="display: inline"> 已通过</div>
            <br>
            操作：
            <button type="button" class="btn btn-outline-danger" style="font-size: 15px" @click="infoDelete(name)">删除</button>
          </div>

          <br>
          <div class="kp">
            名称：
            <div style="display: inline"> 草鱼</div>
            <br>
            详细页网址：
            <a style="display: inline" href="https://baike.baidu.com/item/%E8%8D%89%E9%B1%BC/680268">https://baike.baidu.com/item/%E8%8D%89%E9%B1%BC/680268</a>
            <br>
            状态：
            <div style="display: inline"> 已通过</div>
            <br>
            操作：
            <button type="button" class="btn btn-outline-danger" style="font-size: 15px" @click="infoDelete(name)">删除</button>
          </div>

          <br>
        </div>

        <div id="tab2" class=scrollable-div>
          <table class="table table-hover   text-center">
            <thead class="table-primary" style="font-size: 25px">
            <tr>
              <th>用户名</th>
              <th>手机号码</th>
              <th>身份类型</th>
              <th>操作</th>
            </tr>
            </thead>

            <tbody style="font-size: 20px">
            <tr v-for="acc in account" :key="acc.usernamae">
              <td>{{ acc.username }}</td>
              <td>{{ acc.telephone }}</td>
              <td>{{ acc.identity }}</td>
              <td>
                <button type="button" class="btn btn-outline-primary" style="font-size: 15px;height: 30px" @click="accControl(acc.username,'删除')">删除</button>
                &nbsp
                <button type="button" class="btn btn-outline-danger" style="font-size: 15px;height: 30px" @click="accControl(acc.username, '重置')">重置</button>
              </td>
            </tr>
            </tbody>
          </table>
        </div>

        <div id="tab3" class=scrollable-div>
          <table class="table table-hover   text-center">
            <thead class="table-primary" style="font-size: 25px">
            <tr>
              <th>商品id</th>
              <th>商品名</th>
              <th>价格</th>
              <th>操作</th>
              <th>备注</th>
            </tr>
            </thead>

            <tbody style="font-size: 20px">

            <tr v-for="mer in merchant" :key="mer.id">
              <td> {{ mer.id }}</td>
              <td>{{ mer.name }}</td>
              <td>{{ mer.price }}</td>
              <td>
                <button type="button" class="btn btn-outline-primary" style="font-size: 15px;height: 30px" @click="audit(mer.id,'yes',mer.remark)">通过</button>
                &nbsp
                <button type="button" class="btn btn-outline-danger" style="font-size: 15px;height: 30px" @click="audit(mer.id,'no',mer.remark)">不通过</button>
              </td>
              <td><input type="text" placeholder="备注" v-model="mer.remark"></td>
            </tr>

            </tbody>
          </table>
        </div>

        <div id="tab4" class=scrollable-div>
          <table class="table table-hover   text-center">
            <thead class="table-primary" style="font-size: 25px">
            <tr>
              <th>ID</th>
              <th>主题</th>
              <th>问题</th>
              <th>应答</th>
              <th>确认</th>
            </tr>
            </thead>

            <tbody style="font-size: 20px">
            <tr v-for="msg in message">
              <td>{{ msg.id }}</td>
              <td>{{ msg.subject }}</td>
              <td>{{ msg.info }}</td>
              <td>
                <label>
                  <textarea type="text" placeholder="回复内容" style="font-size: 15px" v-model="msg.reply"></textarea>
                </label>
              </td>

              <td>
                <button type="button" class="btn btn-outline-primary" style="font-size: 20px" @click="reply(msg.id, msg.reply)">回复</button>
              </td>
            </tr>
            </tbody>
          </table>
        </div>

      </section>

    </section>
  </div>
</template>
<script>
import axios from "axios";

export default {
  name: "Administrator",
  data() {
    return {
      info: [],
      account: [],
      merchant: [],
      message: [],
    };
  },
  methods: {
    goBack() {
      this.$router.push({path: '/'})
    },
    async accControl(username, oper) {
      const formData = new FormData()
      formData.append('username', username)
      formData.append('oper', oper)
      await axios
          .post('http://127.0.0.1:9999/AccControl/', formData)
          .then(response => {
            this.refresh()
          }).catch(error => {
          })
    },
    async infoDelete(name) {
      const formData = new FormData()
      formData.append('name', name)
      await axios
          .post('http://127.0.0.1:9999/InfoDelete/', formData)
          .then(response => {
            this.refresh()
          }).catch(error => {
          })
    },

    async audit(id, oper, remark) {
      const formData = new FormData()
      formData.append('id', id)
      formData.append('status', oper)
      formData.append('remark', remark)
      await axios
          .post('http://127.0.0.1:9999/Audit/', formData)
          .then(response => {
            this.refresh()
          }).catch(error => {
          })
    },
    async reply(id, rep) {
      const formData = new FormData()
      formData.append('id', id)
      formData.append('reply', rep)
      await axios
          .post('http://127.0.0.1:9999/Reply/', formData)
          .then(response => {
            this.refresh()
          }).catch(error => {
          })
    },
    async refresh() {
      await axios
          .post('http://127.0.0.1:9999/Admin/')
          .then(response => {
            this.info = response.data.data['info']
            this.account = response.data.data['account']
            this.merchant = response.data.data['merchant']
            this.message = response.data.data['message']
          }).catch(error => {
          })
    }
  },
  async mounted() {
    this.refresh()
  },
}
</script>
<style>
.scrollable-div {
  height: 400px;
  overflow-y: auto; /* 只允许垂直滚动 */
}

.kp {
  width: 1000px;
  height: 200px;
  border-radius: 15px;
  background-color: #e0e0e0;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  padding: 20px;
  text-align: left;
  font-size: 20px;
  color: #2c0b0e;
}
</style>