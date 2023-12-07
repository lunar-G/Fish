<script>
import axios from "axios";

export default {
  name: "Recommend",
  data() {
    return {
      username: '',
      recommend: [],
      habit: [],
      illustrated: [],
      commodity: [],
      order: [],
      cart: [],
      message: [],
      user: [],
      selected: [],
      medicine: ['敌百虫:0.75克/立方米', '阿维菌素:15毫升/立方米', '伊维菌素:20毫升/立方米', '溴氰菊酯:0.25克/亩', '氯氰菊酯:0.5克/亩',
        '硫酸铜:0.6克/立方米', '甲苯咪唑:1.0克/立方米', '阿苯达唑:0.1毫克/斤', '辛硫磷:12克/亩'],
      name: '',
      email: '',
      subject: '',
      info: '',
      tab: ['tab1', 'tab2', 'tab3', 'tab4'],
      type: '',
      temperature: '',
      fishWeight: '',
      oneselected: '',
      weight: [0, 0],
      one: true,
      two: false,
      drug: '',
    }
  },
  async mounted() {
    this.username = this.$route.query.username
    await this.refresh()
    this.init()
  },
  watch: {
    a() {
      this.compute;
    },
  },
  methods: {
    compute() {
      let weight = this.fishWeight
      if (this.temperature === '20°以上') {
        weight = weight * 0.05
      } else if (this.temperature === '20°以下') {
        weight = weight * 0.03
      }
      let a = 0
      if (this.type === '单一养殖') {
        a = 0.8
      } else if (this.type === '混合养殖') {
        a = 0.4
      }
      this.weight[0] = (weight * a).toFixed(2)
      this.weight[1] = (weight * (1 - a)).toFixed(2)
    },
    oneortwo() {
      if (this.type === '单一养殖') {
        this.one = true
        this.two = false
      } else if (this.type === '混合养殖') {
        this.one = false
        this.two = true
      }
    },
    goBack() {
      this.$router.push({path: '/'})
    },
    async save() {
      const formData = new FormData();
      formData.append('username', this.username);
      formData.append('identity', this.identity);
      formData.append('telephone', this.user.telephone);
      formData.append('province', this.user.province);
      formData.append('area', this.user.area);
      formData.append('species', this.user.species);
      await axios
          .post('http://127.0.0.1:9999/Save/', formData)
          .then(response => {
            this.refresh()
          }).catch(error => {
          })
    },
    async del(id, type) {
      const formData = new FormData();
      formData.append('id', id);
      formData.append('type', type);
      await axios
          .post('http://127.0.0.1:9999/Delete/', formData)
          .then(response => this.refresh()).catch(error => {
          })
    },
    init() {
      const center = new TMap.LatLng(31.945796, 112.082888);
      const map = new TMap.Map(document.getElementById('map'), {
        center: center,
        zoom: 15,
      });
      const markerLayer = new TMap.MultiMarker({
        map: map,
        styles: {
          "myStyle": new TMap.MarkerStyle({
            "width": 25,
            "height": 35,
            "src": '../src/assets/microsoft.png',
            "anchor": {x: 16, y: 32}
          })
        },
        geometries: [{
          "id": "1",
          "styleId": 'myStyle',
          "position": new TMap.LatLng(31.945796, 112.082888),
          "properties": {
            "title": "marker1"
          }
        },]
      });
    },
    async refresh() {
      const formData = new FormData();
      formData.append('username', this.username);
      await axios
          .post('http://127.0.0.1:9999/GetDatas/', formData)
          .then(response => {
            this.recommend = response.data.data['recommend']
            this.habit = response.data.data['habit']
            this.illustrated = response.data.data['illustrated']
            this.commodity = response.data.data['commodity']
            this.order = response.data.data['order']
            this.cart = response.data.data['cart']
            this.message = response.data.data['message']
            this.user = response.data.data['user']
          }).catch(error => {
          })
    },
    async settlement(id) {
      const formData = new FormData();
      formData.append('id', id);
      await axios
          .post('http://127.0.0.1:9999/Settlement/', formData)
          .then(response => {
            this.refresh()
          }).catch(error => {
          })
    },
    pharmaceuticals(number) {
      this.drug = this.medicine[number - 1]
    },
    async buyAndCart(id, type) {
      if (type === '购物车') {
        alert('加入成功!')
      } else (alert('购买成功！'))
      const formData = new FormData();
      formData.append('id', id);
      formData.append('username', this.username);
      formData.append('type', type);
      await axios
          .post('http://127.0.0.1:9999/BuyAndCart/', formData)
          .then(response => this.refresh()).catch(error => {
          })
    },
    async sendMessage() {
      const formData = new FormData();
      formData.append('username', this.username);
      formData.append('name', this.name);
      formData.append('subject', this.subject);
      formData.append('email', this.email);
      formData.append('info', this.info);
      await axios
          .post('http://127.0.0.1:9999/SendMessage/', formData)
          .then(response => this.refresh()).catch(error => {
          })
    },
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
        <li style="color: wheat;font-size: 18px">用户名：{{ this.user.username }}</li>
        <li style="color: wheat;font-size: 18px">身份类型：{{ this.user.identity }}</li>
        <li>
          <a href="#projects">
            <span class="rect"></span>
            <span class="circle"></span>
            养殖推荐
          </a>
        </li>
        <li>
          <a href="#featured">
            <span class="rect"></span>
            <span class="circle"></span>
            鱼类习性
          </a>
        </li>
        <li>
          <a href="#blog">
            <span class="rect"></span>
            <span class="circle"></span>
            疾病诊断
          </a>
        </li>
        <li>
          <a href="#buy">
            <span class="rect"></span>
            <span class="circle"></span>
            产品购买
          </a>
        </li>
        <li>
          <a href="#video">
            <span class="rect"></span>
            <span class="circle"></span>
            个人信息
          </a>
        </li>
        <li>
          <a href="#contact">
            <span class="rect"></span>
            <span class="circle"></span>
            联系我们
          </a>
        </li>
        <li style="color: wheat;font-size: 18px" id="leave" @click="goBack">退出登录</li>
      </ul>
    </nav>
  </div>
  <div class="slider">
    <div class="Modern-Slider content-section" id="top">

      <div class="item item-1">
        <div class="img-fill">
          <div class="image" style="background-image: url(/src/assets/image/slide2.jpg)"></div>
          <div class="info">
            <div>
            </div>
          </div>
        </div>
      </div>

      <div class="item item-2">
        <div class="img-fill">
          <div class="image" style="background-image: url(/src/assets/image/slide3.jpg)"></div>
          <div class="info">
            <div>
            </div>
          </div>
        </div>
      </div>

      <div class="item item-3">
        <div class="img-fill">
          <div class="image" style="background-image: url(/src/assets/image/slide1.jpg)"></div>
          <div class="info">
            <div>
            </div>
          </div>
        </div>
      </div>

    </div>
  </div>
  <div class="page-content">

    <section id="projects" class="content-section">


      <div class="section-heading">
        <h1>养殖<br><em>推荐</em></h1>
        <p>我国水产养殖业发达并不成熟，可供我们养殖的品种很多，
          <br>下图分别为鲤鱼、鲫鱼、草鱼、青鱼和鲶鱼，可点击查看详情。</p>
      </div>

      <div class="section-content">
        <div class="masonry">
          <div class="row">

            <div v-for="item in this.recommend.slice(0,1)" class="item">
              <div class="item">
                <div class="col-md-8">
                  <a :href="item['detailUrl']"><img :src="item['imgUrl']" alt=""></a>
                </div>
              </div>
            </div>

            <div v-for="item in this.recommend.slice(1,4)" class="item">
              <div class="item">
                <div class="col-md-4">
                  <a :href="item['detailUrl']"><img :src="item['imgUrl']" alt=""></a>
                </div>
              </div>
            </div>

            <div v-for="item in this.recommend.slice(4,5)" class="item">
              <div class="item">
                <div class="col-md-8">
                  <a :href="item['detailUrl']"><img :src="item['imgUrl']" alt=""></a>
                </div>
              </div>
            </div>

          </div>
        </div>
      </div>
      <div class="section-heading border border-primary" style="height:300px">
        <b-row>
          <b-col lg="6">
            <b-row style="margin-left:20px;" @change="compute">
              <b-col lg="12">
                <div class="form-check form-check-inline">
                  <input type="radio" id="one" value="20°以上" v-model="temperature" class="form-check-input">
                  <label for="one" class="form-check-label" style="font-size:15px">20°以上</label><br/>
                </div>
                <div class="form-check form-check-inline">
                  <input type="radio" id="two" value="20°以下" v-model="temperature" class="form-check-input">
                  <label for="two" class="form-check-label" style="font-size:15px">20°以下</label><br/>
                </div>
              </b-col>
              <b-col lg="12">
                <div class="form-check form-check-inline">
                  <input type="radio" id="two" value="单一养殖" v-model="type" class="form-check-input" @click="oneortwo">
                  <label for="two" class="form-check-label" style="font-size:15px">单一养殖</label><br/>
                </div>
                <div class="form-check form-check-inline">
                  <input type="radio" id="one" value="混合养殖" v-model="type" class="form-check-input" @click="oneortwo">
                  <label for="one" class="form-check-label" style="font-size:15px">混合养殖</label><br/>
                </div>

              </b-col>
              <b-col lg="3" style="margin-left:50px" v-show="one">
                <div class="form-check">
                  <input class="form-check-input" type="radio" id="鲤鱼" v-model="oneselected" value="鲤鱼">
                  <label class="form-check-label" for="鲤鱼" style="font-size:15px">鲤鱼</label>
                </div>
                <div class="form-check ">
                  <input class="form-check-input" type="radio" id="鲫鱼" v-model="oneselected" value="鲫鱼">
                  <label class="form-check-label" for="鲫鱼" style="font-size:15px">鲫鱼</label>
                </div>
                <div class="form-check ">
                  <input class="form-check-input" type="radio" id="青鱼" v-model="oneselected" value="青鱼">
                  <label class="form-check-label" for="青鱼" style="font-size:15px">青鱼</label>
                </div>
                <div class="form-check ">
                  <input class="form-check-input" type="radio" id="鲢鱼" v-model="oneselected" value="鲢鱼">
                  <label class="form-check-label" for="鲢鱼" style="font-size:15px">鲢鱼 </label>
                </div>
                <div class="form-check ">
                  <input class="form-check-input" type="radio" id="草鱼" v-model="oneselected" value="草鱼">
                  <label class="form-check-label" for="草鱼" style="font-size:15px"> 草鱼</label>
                </div>
              </b-col>
              <b-col lg="3" style="margin-left:50px" v-show="two">
                <div class="form-check form-switch">
                  <input class="form-check-input" type="checkbox" id="鲤鱼" v-model="selected" value="鲤鱼">
                  <label class="form-check-label" for="鲤鱼" style="font-size:15px">鲤鱼</label>
                </div>
                <div class="form-check form-switch">
                  <input class="form-check-input" type="checkbox" id="鲫鱼" v-model="selected" value="鲫鱼">
                  <label class="form-check-label" for="鲫鱼" style="font-size:15px">鲫鱼</label>
                </div>
                <div class="form-check form-switch">
                  <input class="form-check-input" type="checkbox" id="青鱼" v-model="selected" value="青鱼">
                  <label class="form-check-label" for="青鱼" style="font-size:15px">青鱼</label>
                </div>
                <div class="form-check form-switch">
                  <input class="form-check-input" type="checkbox" id="鲢鱼" v-model="selected" value="鲢鱼">
                  <label class="form-check-label" for="鲢鱼" style="font-size:15px">鲢鱼 </label>
                </div>
                <div class="form-check form-switch">
                  <input class="form-check-input" type="checkbox" id="草鱼" v-model="selected" value="草鱼">
                  <label class="form-check-label" for="草鱼" style="font-size:15px"> 草鱼</label>
                </div>
              </b-col>
              <label style="font-size:15px">鱼重：<input type="text" v-model="fishWeight" style="font-size:15px;width:50px;height:15px">Kg</label>
            </b-row>
            <b-row style="margin-left:20px">
              <div style="font-size:18px;">
                <h>应投饲料:</h>
                <div style="display: inline-block;" class="text-primary">膨化料</div>
                <span class="badge badge-primary"> {{ weight[0] }}斤</span>
                <div style="display: inline-block;" class="text-primary">颗粒料</div>
                <span class="badge badge-primary"> {{ weight[1] }}斤</span>
              </div>
            </b-row>
          </b-col>

          <b-col lg="5" style="margin-left:20px;heitght:250px" class="border">
            <div class="dropdown">
              <button type="button" class="btn btn-danger dropdown-toggle btn-lg" data-bs-toggle="dropdown" aria-expanded="false">
                药物选择
              </button>
              <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton">
                <li>
                  <button class="dropdown-item" @click="pharmaceuticals(1)">敌百虫</button>
                </li>
                <li>
                  <button class="dropdown-item" @click="pharmaceuticals(2)">阿维菌素</button>
                </li>
                <li>
                  <button class="dropdown-item" @click="pharmaceuticals(3)">伊维菌素</button>
                </li>
                <li>
                  <button class="dropdown-item" @click="pharmaceuticals(4)">溴氰菊酯</button>
                </li>
                <li>
                  <button class="dropdown-item" @click="pharmaceuticals(5)">氯氰菊酯</button>
                </li>
                <li>
                  <button class="dropdown-item" @click="pharmaceuticals(6)">硫酸铜</button>
                </li>
                <li>
                  <button class="dropdown-item" @click="pharmaceuticals(7)">甲苯咪唑</button>
                </li>
                <li>
                  <button class="dropdown-item" @click="pharmaceuticals(8)">阿苯达唑</button>
                </li>
                <li>
                  <button class="dropdown-item" @click="pharmaceuticals(9)">辛硫磷</button>
                </li>

              </ul>
            </div>
            <div style="height:20px"></div>
            <div style="height:20px;font-size:20px">药物用法:</div>
            <div style="height:150px;font-size:25px" class="text-info">{{ drug }}</div>
          </b-col>
        </b-row>
      </div>
    </section>

    <section id="featured" class="content-section">
      <div class="section-heading">
        <h1>鱼类<br><em>特性</em></h1>
        <p>不同的鱼类有不同的特点
          <br>这里简单说明几种不同淡水鱼的特点</p>
      </div>
      <div class="section-content">
        <div class="owl-carousel owl-theme">

          <div class="item">
            <div class="image">
              <img src="/src/assets/image/ly.jpg" alt="">
            </div>
            <div class="text-content">
              <h4 class="text-center">鲤鱼</h4>
              <p class="text-justify">鲤鱼体型短粗，口呈马蹄形，吻朝下似亲嘴状，唇厚，两根须，尾鳍红色或微红或黄色，
                背鳍和臀鳍均有一根粗壮带锯齿的硬棘，侧线鳞33-39。
                鲤鱼属于杂食性鱼类，底层鱼类，荤素兼食，食性杂，食量大，有拱泥觅食的习惯，故有一定的"改底"作用。
                一般亩放800-2000尾。</p>
            </div>
          </div>

          <div class="item">
            <div class="image">
              <img src="/src/assets/image/jy.jpg" alt="">
            </div>
            <div class="text-content">
              <h4 class="text-center">鲫鱼</h4>
              <p class="text-justify">鲫鱼属小型鱼类，体型较小，以植物为主食的杂食性鱼类，能适应各种劣质水域，
                耐低氧，食性杂，一年四季都能觅食，喜群聚，生长速度较慢。鲫鱼品种繁多，优质鲫鱼的侧线鳞必须在29片(枚)
                鳞甲以上，多者为35片(枚)鳞甲甚至以上，如果少于或等于28片(枚)鳞甲则为土鲫或者至少为劣质鲫鱼，总之，鲫鱼的侧线鳞甲
                片数目越多越好越肯长。一般亩放2000-5000尾。</p>
            </div>
          </div>

          <div class="item">
            <div class="image">
              <img src="/src/assets/image/cy.jpg" alt="">
            </div>
            <div class="text-content">
              <h4 class="text-center">草鱼</h4>
              <p class="text-justify">草鱼的生长很快，在内陆水域算长势最快的品种之一。草鱼，顾名思义，
                以草料为主要食物，在自然状态下成鱼以吃水草为主，是典型的草食性鱼类。草鱼是中层鱼类，
                其生长迅速、饲料来源广。一般亩放500-1000尾。</p>
            </div>
          </div>

          <div class="item">
            <div class="image">
              <img src="/src/assets/image/qy.jpg" alt="">
            </div>
            <div class="text-content">
              <h4 class="text-center">青鱼</h4>
              <p class="text-justify">青鱼是中下层鱼类，长势快，体型大，性子急，属肉食性
                兼杂食性鱼类，常以螺蛳、河蚌、甲壳类等底栖动物及有壳动物为食，至今没有发现有吃食鱼类的现象。
                青鱼一般亩放500-1000尾，混养清吃底栖螺蚌，亩放30-50尾。</p>
            </div>
          </div>

          <div class="item">
            <div class="image">
              <img src="/src/assets/image/ny.jpg" alt="">
            </div>
            <div class="text-content">
              <h4 class="text-center">鲶鱼</h4>
              <p class="text-justify">鲢鱼是上层鱼类，以水里浮游生物中的浮游植物及藻类为食，是典型的滤食性鱼种，
                故鳃耙细而密，同侧鳃耙彼此相连呈海绵状膜质片，利于滤取微细食物。白鲢因其食性特殊---滤食水生藻类，
                能净化水质，有“水中清道夫”雅称的特殊鱼种，混养恰当的比例(比如亩放100-300尾)时，有调节水质的作用，
                对抑制蓝藻暴发有特别的效果。因此，现代池塘养鱼都须混养鲢鱼，可保水质无忧！一般亩放500-800尾，混养，亩放100-300尾。</p>
            </div>
          </div>

          <div class="item">
            <div class="image">
              <img src="/src/assets/image/yy.jpg" alt="">
            </div>
            <div class="text-content">
              <h4 class="text-center">鳙鱼</h4>
              <p class="text-justify">鳙鱼头大而且宽，口也很宽大，且稍微上翘。头长大于体高。吻短而圆钝。
                口大，端位，口裂向上倾斜，下颌稍突出，口角可达眼前缘垂直线之下，上唇中间部分很厚。眼位比较低。
                鳃耙数目很多，呈叶状，排列极为紧密，但不连合。腹部在腹鳍基部之前较圆，其后部至肛门前有狭窄的腹棱。
                鳙鱼背部及体侧上半部微黑，有许多不规则的黑色斑点；腹部灰白色。各鳍呈灰色，上有许多黑色小斑点，故名"花"鲢。
                有专养鳙鱼技术的，可以亩放400-600尾，混养，亩放50-100尾。
              </p>
            </div>
          </div>

          <div class="item">
            <div class="image">
              <img src="/src/assets/image/by.jpg" alt="">
            </div>
            <div class="text-content">
              <h4 class="text-center">鳊鱼</h4>
              <p class="text-justify">
                民间俗称的鳊鱼，一般是指武昌鱼。武昌鱼学名团头鲂（Megalobrama amblycephala），别名鳊鱼
                、鲂鱼。它的食性同草鱼，是以草食为主的杂食性鱼类，主要以草，藻类为食，属于中小型鱼类。
              </p>
            </div>
          </div>


        </div>
      </div>

    </section>

    <section id="blog" class="content-section">
      <div class="section-heading">
        <h1>疾病<br><em>诊断</em></h1>
        <p>淡水鱼养殖类常见疾病的相关诊断
          <br>淡水鱼养殖类常见疾病的相关治疗方法</p>
      </div>

      <div class="section-content">
        <div class="tabs-content">
          <div class="wrapper">
            <ul class="tabs clearfix" data-tabgroup="first-tab-group">
              <!--              <li v-for="(item,index) in illustrated"><a :href="'#tab'+(1+index)">{{ item.diseasetype }}</a></li>-->
              <li><a href="#tab1" class="active">病毒性疾病</a></li>
              <li><a href="#tab2">细菌性疾病</a></li>
              <li><a href="#tab3">寄生虫性疾病</a></li>
              <li><a href="#tab4">人为不良因素</a></li>
            </ul>

            <section id="first-tab-group" class="tabgroup ">
              <div :id="'tab'+(1+index)" v-for="(item,index) in illustrated">
                <ul>
                  <li>
                    <div class="item">
                      <img :src="item.img1" alt="">
                      <div class="text-content">
                        <h4>疾病介绍</h4>
                        <p class="text-indent text-justify">{{ item.introduce }}</p>
                      </div>
                    </div>
                  </li>
                  <li>
                    <div class="item">
                      <img :src="item.img2" alt="">
                      <div class="text-content">
                        <h4>解决方法</h4>
                        <p class="text-indent text-justify">{{ item.method }}</p>

                      </div>
                    </div>
                  </li>
                </ul>
              </div>


            </section>

          </div>
        </div>
      </div>

    </section>

    <section id="buy" class="content-section">

      <div class="section-heading">
        <h1>产品<br><em>购买</em></h1>
        <p>本网站提供各种淡水鱼鱼苗以及养殖相关设施
          <br>您可以浏览网页来选择自己所需的物品</p>
      </div>

      <div class="row">

        <div class="col-md-4 mb-4 " v-for="item in this.commodity">
          <div class="card">
            <img :src="item.imgUrl" class="card-img-top" style="width: 320px" alt="淡水鱼3">
            <div class="card-body">
              <h5 class="card-title" style="width: 100px;font-size: 15px">{{ item.name }}</h5>
              <p class="card-text" style="width: 100px;font-size: 15px">价格: ￥{{ item.price }}</p>
            </div>
            <div>
              <button class="btn btn-primary" style="width: 100px;font-size: 15px" @click="buyAndCart(item.id,'购物车')">加入购物车</button>
              <button class="btn btn-success m-lg-1" style="width: 100px;font-size: 15px" @click="buyAndCart(item.id,'购买')">直接购买</button>
            </div>
          </div>
        </div>

      </div>

    </section>

    <section id="video" class="content-section" style="font-size: 15px">

      <div class="row" style="">
        <div class="col-md-10 offset-md-1" style=" align-items: center;">
          <div class="card">
            <div class="card-header " style="background-color:#45489a;color: white ">
              <h2 style="width: 600px">我的购物车</h2>
            </div>
            <div class="card-body" style="width: 600px">

              <ul class="list-group">
                <li class="list-group-item d-flex justify-content-between align-items-center" v-for="item in this.cart">
                  物品：{{ item.item }}&nbsp&nbsp&nbsp&nbsp数量：{{ item.number }}&nbsp&nbsp&nbsp&nbsp共计：{{ item.price }}元
                  <div>
                    <button class="btn btn-success" style="font-size: 18px;margin-right:10px" @click="settlement(item.id)">结算</button>
                    <button class="btn btn-warning" style="font-size: 18px" @click="del(item.id,'购物车')">删除</button>
                  </div>
                </li>
              </ul>

            </div>

          </div>
        </div>
      </div>
      <br>

      <div class="row">
        <div class="col-md-10 offset-md-1" style=" align-items: center;">
          <div class="card">
            <div class="card-header" style="background-color:#45489a;color: white ">
              <h2 style="width: 600px">我的订单</h2>
            </div>
            <div class="card-body" style="width: 600px">
              <ul class="list-group">
                <li class="list-group-item d-flex justify-content-between align-items-center" v-for="item in this.order">
                  {{ item.item }}×{{ item.number }}&nbsp&nbsp&nbsp&nbsp订单金额&nbsp¥{{ item.price }}&nbsp&nbsp {{ item.status }}
                  <button class="btn btn-danger" @click="del(item.id,'订单')" style="background-color: #45489a;font-size: 18px;">删除</button>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
      <br>
      <div class="row">
        <div class="col-md-10 offset-md-1" style=" align-items: center;">
          <div class="card">
            <div class="card-header" style="background-color:#45489a;color: white ">
              <h2 style="width: 600px">个人信息</h2>
            </div>
            <div class="card-body" style="width: 600px">
              <ul class="list-group">
                <li class="list-group-item d-flex justify-content-between align-items-center">
                  <label>账号：{{ this.user.username }}</label><br><br>
                  <button class="btn btn-close-white" style="font-size: 18px;color: white">1</button>
                </li>
                <li class="list-group-item d-flex justify-content-between align-items-center">
                  <label>身份类型：{{ this.user.identity }}</label><br><br>
                  <button class="btn btn-close-white" style="font-size: 18px;color: white">1</button>
                </li>
                <li class="list-group-item d-flex justify-content-between align-items-center">
                  <label>手机号：<input type="text" v-model="this.user.telephone" style="background-color:transparent"></label><br><br>
                </li>
                <li class="list-group-item d-flex justify-content-between align-items-center">
                  <label>省份：<input type="text" v-model="this.user.province" style="background-color:transparent"></label><br><br>
                </li>
                <li class="list-group-item d-flex justify-content-between align-items-center">
                  <label>养殖面积(亩)：<input type="text" v-model="this.user.area" style="background-color:transparent"></label><br><br>
                </li>
                <li class="list-group-item d-flex justify-content-between align-items-center">
                  <label>养殖品种：<input type="text" v-model="this.user.species" style="background-color:transparent"></label><br><br>
                </li>
                <li>
                  <button class="btn btn-primary" style="font-size: 18px" @click="save">保存</button>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>

    </section>

    <section id="contact" class="content-section">


      <div id="contact-content">

        <div class="section-heading">
          <h1>联系<br><em>我们</em></h1>
          <p>公司位于湖北省襄阳市湖北理工学院文理学院
            <br>您也可以线上发送信息与我们取得联系</p>
        </div>

        <div id="map" style="width:100%; height:400px;border: 0 "></div>
        <br>

        <div class="section-content">
          <div class="row">
            <div class="col-md-3">
              <fieldset>
                <input name="name" type="text" class="form-control" v-model="name" id="name" placeholder="您的姓名..." required="" style="width: 200px">
              </fieldset>
            </div>
            <div class="col-md-3">
              <fieldset>
                <input name="email" type="email" class="form-control" v-model="email" id="email" placeholder="您的邮箱..." required="" style="margin-left: 30px">
              </fieldset>
            </div>
            <div class="col-md-3">
              <fieldset>
                <input name="subject" type="text" class="form-control" v-model="subject" id="subject" placeholder="主题..." required="" style="width: 300px;margin-left: 80px">
              </fieldset>
            </div>

            <div class="col-md-12">
              <fieldset>
                <textarea name="message" rows="6" class="form-control" v-model="info" id="message" placeholder="请输入内容..." required=""></textarea>
              </fieldset>
            </div>
            <div class="col-md-12">
              <fieldset>
                <button type="submit" id="form-submit" class="btn" @click="sendMessage">发送</button>
              </fieldset>
            </div>
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