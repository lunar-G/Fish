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
      name: '',
      email: '',
      subject: '',
      info: '',
    };
  },
  async mounted() {
    this.username = this.$route.query.username
    await this.refresh()
    this.init()
  },
  methods: {
    goBack() {
      this.$router.push({path: '/'})
    },
    add(id) {
      alert(event.target.parentNode.parentNode.childNodes[1].textContent)
    },
    buy(id) {
      alert(event.target.parentNode.parentNode.childNodes[1].textContent)
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
        map: map,  //指定地图容器
        styles: {
          "myStyle": new TMap.MarkerStyle({
            "width": 25,
            "height": 35, // 点标记样式高度（像素）
            "src": '../src/assets/microsoft.png',  //图片路径
            "anchor": {x: 16, y: 32}
          })
        },
        geometries: [{
          "id": "1",   //点标记唯一标识，后续如果有删除、修改位置等操作，都需要此id
          "styleId": 'myStyle',  //指定样式id
          "position": new TMap.LatLng(31.945796, 112.082888),  //点标记坐标位置
          "properties": {//自定义属性
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
    async settlement() {
      const formData = new FormData();
      formData.append('username', this.username);
      await axios
          .post('http://127.0.0.1:9999/Settlement/', formData)
          .then(response => {
            this.refresh()
          }).catch(error => {
          })
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
        <h1>养殖<br><em>品种</em></h1>
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
              <li><a href="#tab1" class="active">病毒性疾病</a></li>
              <li><a href="#tab2">细菌性疾病</a></li>
              <li><a href="#tab3">寄生虫性疾病</a></li>
              <li><a href="#tab4">人为不良因素</a></li>
            </ul>

            <section id="first-tab-group" class="tabgroup">

              <div id="tab1">
                <ul>
                  <li>
                    <div class="item">
                      <img src="/src/assets/image/bd1.jpg" alt="">
                      <div class="text-content">
                        <h4>疾病介绍</h4>
                        <p class="text-indent text-justify">病毒性疾病指的是由于病毒入侵所造成的疾病，在淡水养殖鱼类中，经常会有病毒性疾病的出
                          现。举例来说，最容易发生病毒性疾病的物种之一是草鱼，而在众多疾病中，草鱼最容易感染的是出
                          血病。患上出血病的草鱼，一般其腮部、头顶、眼眶
                          周围会出现充血的现象，而整个鱼体颜色变暗变
                          黑。患上出血病的草鱼很容易死去，一般而言，一旦
                          患上这种病，草鱼的死亡率可达到 70%以上，并且
                          发病周期短，2~3天内便会死亡。</p>
                      </div>
                    </div>
                  </li>

                  <li>
                    <div class="item">
                      <img src="/src/assets/image/bd2.jpg" alt="">
                      <div class="text-content">
                        <h4>解决方法</h4>
                        <p class="text-indent text-justify">以病毒性疾病中较为常见的出血病为例，出血病经常发生在草鱼鱼群中，
                          目前针对这种病症，主要采取的是以预防为主的措
                          施。如养殖户可以对鱼塘或鱼池进行定期消毒，如
                          投放生石灰、漂白粉等，或者定期对鱼塘进行清淤，
                          以保持鱼群生长环境的整洁。此外，在对小鱼苗进
                          行筛选时，养殖户可以选取更加健康的小鱼苗，并
                          且在投入鱼塘之前对其进行杀菌处理。</p>

                      </div>
                    </div>
                  </li>
                </ul>
              </div>
              <div id="tab2">
                <ul>
                  <li>
                    <div class="item">
                      <img src="/src/assets/image/xj1.jpg" alt="">
                      <div class="text-content">
                        <h4>疾病介绍</h4>
                        <p class="text-indent text-justify"> 细菌性疾病指的是由于细菌感染而引发的疾
                          病，在淡水养殖中，一些鱼类也时常面临细菌性疾
                          病的威胁。如草鱼经常患上细菌性出血病，一旦患
                          上这种病，草鱼首先会出现轻度出血的症状，如在
                          口腔、鳍基等部位发生出血；其次一旦病情逐渐变
                          严重，一些草鱼甚至会出现整个体表出血的症状，
                          并且腹部也会逐渐膨大开来，某些部位出现红斑
                          点。此外，鲤和草鱼也非常容易患上烂鳃病，一旦患
                          上这种病，鱼类首先会出现游动较慢、头部变黑、食
                          欲下降的症状，而随着病情逐渐变严重，通过对病
                          鱼鳃部的观察，可以明显看到其鳃部出现泥灰色的
                          斑点，或者整个鳃部呈蜡黄色。当然，在对细菌性疾
                          病进行观察时，要将其与一些类似的寄生虫病进行
                          明显划分。</p>

                      </div>
                    </div>
                  </li>
                  <li>
                    <div class="item">
                      <img src="/src/assets/image/xj2.jpg" alt="">
                      <div class="text-content">
                        <h4>解决方法</h4>
                        <p class="text-indent text-justify"> 以常见的细菌性疾
                          病——细菌性出血病为例，一般而言，在发生这种
                          疾病时，首先要对鱼群进行杀菌处理。此时养殖户
                          要加强对鱼群的管理，如对使用工具进行杀菌处
                          理，以及将特殊药物氯立得喷洒在鱼塘周围等。其
                          次要判定病情的严重程度，如果病情较轻，可以使
                          用抗暴威来进行治疗，而如果病情严重，则要向鱼
                          塘投入鱼血康宁，并且适当增加抗暴威的使用量和
                          使用时长。</p>

                      </div>
                    </div>
                  </li>
                </ul>
              </div>
              <div id="tab3">
                <ul>
                  <li>
                    <div class="item">
                      <img src="/src/assets/image/jsc1.jpg" alt="">
                      <div class="text-content">
                        <h4>疾病介绍</h4>
                        <p class="text-indent text-justify">寄生虫性疾病指的是鱼体内由于出现寄生虫
                          而引发的常见疾病，常见的寄
                          生虫性疾病主要有以下几种：
                          一是粘孢子病，在鲤群内部经常会发生粘孢子病。
                          发病时，鲤的鱼鳍上会出现一种灰白色的胞囊，一些病鱼的眼睛、肠道等部位也会出现相关的胞囊。

                          二是指环虫病，在鳙和鲤群中，也会发生指环虫病。
                          患上这种病的鱼类，其鳃丝上会存在指环虫，而在
                          吃食物时也很容易出现炸群现象。

                          三是车轮虫病，在鲤群内部，有时候也会发生车轮虫病。开始时不易察觉，
                          一旦疾病发展到中期，一些小鱼苗便会出现离开群体、独自狂游的现象，
                          到了后期，小鱼苗会出现呼吸困难、逐渐窒息的情况。

                          四是锚头鳋病，在草鱼群内部可能会出现锚头鳋病。
                          一旦患上这种疾病，草鱼鳞片的光泽便会逐渐变淡，
                          到了中期，鱼体可能会呈现出血的状态，并且伴随着食欲下降、躁动
                          不安的症状。
                        </p>
                      </div>
                    </div>
                  </li>
                  <li>
                    <div class="item">
                      <img src="/src/assets/image/jsc2.jpg" alt="">
                      <div class="text-content">
                        <h4>解决方法</h4>
                        <p class="text-indent text-justify">以淡水养殖鱼类中的
                          鲤为例，鲤经常患上粘孢子病。在治疗这一疾病时，
                          首先，人们可以用生石灰对鱼塘进行消毒处理，通
                          过清洁环境来压迫寄生虫生长的空间。其次，面对
                          患病严重的鱼群，人们可以使用渔丰碘、菌毒克等
                          药物对其进行处理，而面对症状较轻的鱼群，则可
                          以使用晶体敌百虫、孢杀等手段进行处理。</p>
                      </div>
                    </div>
                  </li>
                </ul>
              </div>
              <div id="tab4">
                <ul>
                  <li>
                    <div class="item">
                      <img src="/src/assets/image/qt1.jpg" alt="">
                      <div class="text-content">
                        <h4>操作粗放</h4>
                        <p class="text-indent text-justify">有时候，在鱼类捕捞、储存、运输
                          过程中，人工操作过于粗放。如人们使用带钢叉的
                          工具来捕捞鱼类，可能会破坏鱼类自身的保护膜，
                          给鱼体造成伤害，而在面临水中的病原体时，鱼体
                          造成损伤的鱼类难以抵挡病原体的侵入，从而容易
                          引发疾病。此外，在运输过程中，一旦人们管理不
                          当，如将病鱼和健康鱼类混在同一个集装箱里，病
                          菌就会相互传染，从而使健康鱼类受到病菌侵蚀。</p>
                      </div>
                    </div>
                  </li>
                  <li>
                    <div class="item">
                      <img src="/src/assets/image/qt2.jpg" alt="">
                      <div class="text-content">
                        <h4>饲养密度</h4>
                        <p class="text-indent text-justify">在人为因素中，影响鱼类健康的
                          原因还有饲养密度，饲养密度过大也会对鱼类的健康生长造成威胁。如在水域面积有限的鱼塘之中，
                          人们投放大量小鱼苗，在鱼苗长大的过程中，彼此
                          的生活空间会被进一步挤压，从而使鱼类难以获得
                          应有的游动空间。由于投食有限，鱼类之间对食物
                          的争夺较为激烈，一些小鱼难以获得充足的食物，
                          从而影响自身的生长。此外，在鱼群密集的水域，一
                          旦发生疾病，水域难以稀释相应的病菌，导致鱼类
                          很容易出现大规模感染的现象。</p>
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
                <li class="list-group-item d-flex justify-content-between align-items-center" v-for="item in this.cart">{{ item.id }}
                  物品：{{ item.item }}&nbsp&nbsp&nbsp&nbsp数量：{{ item.number }}&nbsp&nbsp&nbsp&nbsp共计：{{ item.price }}元
                  <button class="btn btn-warning" style="font-size: 18px" @click="del(item.id,'购物车')">删除</button>
                </li>
              </ul>

            </div>
            <button class="btn " style="width: 200px;height: 50px;font-size: 20px;background-color: #1cb25d;color: white" @click="settlement">结算</button>
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
                <li class="list-group-item d-flex justify-content-between align-items-center" v-for="o in this.order">
                  订单id:{{ o.id }}.&nbsp&nbsp&nbsp&nbsp {{ o.item }}×{{ o.number }}&nbsp&nbsp&nbsp&nbsp已支付¥{{ o.price }}
                  <button class="btn btn-danger" @click="del(o.id,'订单')" style="background-color: #45489a;font-size: 18px;">删除</button>
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
          <p>公司位于湖北省襄阳市湖北理工学院
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