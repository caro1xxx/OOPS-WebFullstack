<template>
  <div class="home">
    <div class="container diybodyset">
      <div class="row">
        <!-- 左边 -->
        <div class="col-md-3 d-none d-lg-block " style="padding:3px;margin-bottom:340px;">
          <div class="diyleftbodyset">

          <div class="d-none d-md-block diyleftinside rounded shadow p-3 mb-5 bg-body rounded position-relative">
            <div class="diylefttop border-bottom">
              <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-app-indicator" viewBox="0 0 16 16">
                <path d="M5.5 2A3.5 3.5 0 0 0 2 5.5v5A3.5 3.5 0 0 0 5.5 14h5a3.5 3.5 0 0 0 3.5-3.5V8a.5.5 0 0 1 1 0v2.5a4.5 4.5 0 0 1-4.5 4.5h-5A4.5 4.5 0 0 1 1 10.5v-5A4.5 4.5 0 0 1 5.5 1H8a.5.5 0 0 1 0 1H5.5z"/>
                <path d="M16 3a3 3 0 1 1-6 0 3 3 0 0 1 6 0z"/>
              </svg>
              新闻
            </div>
            <div id="loading" class="diylefttop2" style="visibility:hidden;">
              <div class="row">
                <!-- <keep-alive include='DemoNews,DemoHots'> -->
                  <div class="col-md-10 offset-md-1">
                    <demo-news v-for="dats in data" :send=[dats.id,dats.name,dats.content,dats.auth,dats.create_data]></demo-news>
                  </div>
                <!-- </keep-alive> -->
              </div>
            </div>
            <!-- <div id="donghua" class="d-flex align-items-center position-absolute top-50 start-50 translate-middle" style="visibility:visible;">
              <strong>Loading...</strong>
              <div class="spinner-border ms-auto" role="status" aria-hidden="true"></div>
            </div> -->
          </div>
        <div class="diyleftbottom rounded shadow p-3 bg-body rounded" style="margin-top:5px;">
          <div class="diyleftinside rounded">
            <div class="diylefttop border-bottom">
              <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-bar-chart" viewBox="0 0 16 16">
                <path d="M4 11H2v3h2v-3zm5-4H7v7h2V7zm5-5v12h-2V2h2zm-2-1a1 1 0 0 0-1 1v12a1 1 0 0 0 1 1h2a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1h-2zM6 7a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v7a1 1 0 0 1-1 1H7a1 1 0 0 1-1-1V7zm-5 4a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v3a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1v-3z"/>
              </svg>
              排行榜
            </div>
            <div id="loading2" style="visibility:hidden;" class="row d-flex justify-content-center">
              <div class="col-md-12 col-10">
                  <div>
                    <demo-hots v-for="datas in data2" :send=[datas.id,datas.name,datas.content,datas.auth,datas.create_data]></demo-hots>
                  </div>
              </div>
            </div>
          </div>
        </div>
        </div>
      </div>
      
      <!-- 中间 -->
      <div class="col-lg-6 col-md-8" style="margin-top:4px;margin-bottom:50px;">
        <div class="diymidbodyset diypadding10px shadow p-3 bg-body rounded" style="padding:0px;">
          <div class="diylefttop">
            <div class="diylefttop border-bottom">
              <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-card-text" viewBox="0 0 16 16">
                <path d="M14.5 3a.5.5 0 0 1 .5.5v9a.5.5 0 0 1-.5.5h-13a.5.5 0 0 1-.5-.5v-9a.5.5 0 0 1 .5-.5h13zm-13-1A1.5 1.5 0 0 0 0 3.5v9A1.5 1.5 0 0 0 1.5 14h13a1.5 1.5 0 0 0 1.5-1.5v-9A1.5 1.5 0 0 0 14.5 2h-13z"/>
                <path d="M3 5.5a.5.5 0 0 1 .5-.5h9a.5.5 0 0 1 0 1h-9a.5.5 0 0 1-.5-.5zM3 8a.5.5 0 0 1 .5-.5h9a.5.5 0 0 1 0 1h-9A.5.5 0 0 1 3 8zm0 2.5a.5.5 0 0 1 .5-.5h6a.5.5 0 0 1 0 1h-6a.5.5 0 0 1-.5-.5z"/>
              </svg>
              主要
            </div>
          </div>
          <div id="loading3" style="visibility:hidden;" class="diymidinsidebottom">
            <demo-carousel/>
            <hr>
            <div v-for="datas1 in data3">
              <demo-mains :send=[datas1.id,datas1.name,datas1.content,datas1.auth,datas1.create_data]></demo-mains>
            </div>
            <hr>
            <div class="d-flex justify-content-end">
              <button @click="gotomore" type="button" class="btn btn-primary btn-sm">更多</button>
            </div>
          </div>
        </div>
      </div>
      
      <div class="col-lg-3 col-md-4">
        <div class="diyrightset shadow p-3 bg-body rounded">
          <div class="diylefttop">
            <div class="diylefttop border-bottom">
              <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-bookmark-heart" viewBox="0 0 16 16">
                <path fill-rule="evenodd" d="M8 4.41c1.387-1.425 4.854 1.07 0 4.277C3.146 5.48 6.613 2.986 8 4.412z"/>
                <path d="M2 2a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v13.5a.5.5 0 0 1-.777.416L8 13.101l-5.223 2.815A.5.5 0 0 1 2 15.5V2zm2-1a1 1 0 0 0-1 1v12.566l4.723-2.482a.5.5 0 0 1 .554 0L13 14.566V2a1 1 0 0 0-1-1H4z"/>
              </svg>
              每日推荐工具
            </div>
          </div>
          <div id="loading4" style="visibility:hidden;" class="diymidinsidebottom">
            <div v-for="datas2 in data4">
              <demo-users :send=[datas2.id,datas2.name,datas2.content,datas2.auth,datas2.create_data]></demo-users>
            </div>
              <hr>
              <demo-cards/>
              <hr>
              <demo-exemption/>
          </div>
        </div>
      </div>
    </div>
    <div class="row">
        <div class="col-md-12 d-flex justify-content-center">
            <small style="font-size:10px">Copyright &copy; 2021 OOPS</small>
        </div>
    </div>
      </div>
    <div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import '../assets/css/home.css'
import DemoNews from '@/components/demo_news.vue'
import DemoToasts from '@/components/demo_toasts.vue'
import DemoUsers from '@/components/demo_users.vue'
import DemoCards from '@/components/demo_cards.vue'
import DemoMains from '@/components/demo_mains.vue'
import DemoCarousel from '@/components/demo_carousel.vue'
import DemoHots from '@/components/demo_hots.vue'
import DemoExemption from '@/components/demo_exemption.vue'


export default {
  name: 'Home',
  components: {
    DemoNews,
    DemoToasts,
    DemoUsers,
    DemoCards,
    DemoMains,
    DemoCarousel,
    DemoHots,
    DemoExemption,
  },
  data(){
        return{
            // 这里必须和后端传入的数据格式一模一样
            data:{
              id:"",
              name:"",
              content:"",
              auth:"",
              create_data:"",
            },
            data2:{
              id:"",
              name:"",
              content:"",
              auth:"",
              create_data:"",
            },
            data3:{
              id: "",
              name: "",
              content: "",
              auth: "",
              create_data: ""
            },
            data4:{
              id: "",
              name: "",
              content: "",
              auth: "",
              create_data: ""
            },
            count:0,
        }
    },
    // 监听数据是否加载完成
    watch:{
      count:function(){
        // document.getElementById('donghua').style.visibility="hidden";
        document.getElementById('loading').style.visibility='visible';
        document.getElementById('loading2').style.visibility='visible';
        document.getElementById('loading3').style.visibility='visible';
        document.getElementById('loading4').style.visibility='visible';
      }
    },
    mounted(){
      let __this = this; //定义一个变量
      // News
      this.$axios.get('http://81.68.105.198:8002/api/News/')
        .then(function (response){ //response接收数据对象
        __this.data= response.data; //把接收到的数据对象传入data中
        __this.count++; //加载完数据改变count的值
        })
        .catch(function (error){
          console.log(error);
        });
        // Hots
      this.$axios.get('http://81.68.105.198:8002/api/Hots/')
      .then(function (response){ //response接收数据对象
        __this.data2= response.data; //把接收到的数据对象传入data中
        })
        .catch(function (error){
          console.log(error);
        });
        // collection
      this.$axios.get('http://81.68.105.198:8002/api/Collection/')
      .then(function (response){ //response接收数据对象
        __this.data3= response.data; //把接收到的数据对象传入data中
        })
        .catch(function (error){
          console.log(error);
        });
        // Recommend
      this.$axios.get('http://81.68.105.198:8002/api/Recommend/')
      .then(function (response){ //response接收数据对象
        __this.data4= response.data; //把接收到的数据对象传入data中
        })
        .catch(function (error){
          console.log(error);
        });
      // 查看cookies
      // let istoken = this.$cookies.isKey('token');
      // if (istoken == true)
      // {
      //   let data = {"token":this.$cookies.get('token')};
      //   this.$axios.post('http://81.68.105.198:8002/api/v1/TokenAuthView/',data)
      //   .then(function(response){
      //     __this.$store.commit('GetUserInfo',response.data.data);
      //   })
      //   .catch(function (error){
      //     console.log(error);
      //   });
      // }
    },
    methods:{
      gotomore:function(){
        window.open('http://81.68.105.198:70/#/more/1');
      }
    }
}
</script>

