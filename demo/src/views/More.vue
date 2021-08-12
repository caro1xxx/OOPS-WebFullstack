<template>
  <div>
    <div class="container diybodyset">
      <div class="row">
        <!-- 中间 -->
        <div class="col-md-9">
          <div class="shadow p-3 bg-body rounded center1">
            <div class="diylefttop">
              <div class="diylefttop border-bottom">
                更多
              </div>
            </div>
            <div class="diymidinsidebottom">
              <div class="col-12">
                <div class="tab-content" id="nav-tabContent">
                  <div class="tab-pane fade show active" id="list-home" role="tabpanel" aria-labelledby="list-home-list">
                    
                    <div class="row">
                      <div v-for="dat in data.results" class="col-md-6 col-xl-3 col-lg-4 d-flex justify-content-center leftfloat">
                        <more-choice :send=[dat.id,dat.name,dat.introduce,dat.size,dat.version,dat.content,dat.link,dat.create_data,dat.isshow]></more-choice>
                      </div>
                      <div class="d-flex justify-content-center">
                        <nav aria-label="...">
                          <ul class="pagination">
                            <li class="page-item">
                              <a class="page-link" href="#" tabindex="-1" aria-disabled="true" @click="gotopage1">上</a>
                            </li>
                            <li class="page-item"><a class="page-link" @click="gotopage1" >{{ pagenum1 }}</a></li>
                            <li class="page-item active" aria-current="page"><a class="page-link" @click="gotopage2" >{{ pagenum2 }}</a></li>
                            <li class="page-item"><a class="page-link" @click="gotopage3">{{ pagenum3 }}</a></li>
                            <li class="page-item"><a class="page-link" href="#">...</a></li>
                            <li class="page-item"><a class="page-link" href="#">{{ max_page }}</a></li>
                            <li class="page-item">
                              <a class="page-link" href="#" @click="gotopage3">下</a>
                            </li>
                          </ul>
                        </nav>
                      </div>
                    </div>
                  </div>
                  <div class="tab-pane fade" id="list-profile" role="tabpanel" aria-labelledby="list-profile-list">
                    <div v-for="datas4 in data2.results">
                      <more-donor :send=[datas4.id,datas4.name,datas4.introduce,datas4.size,datas4.version,datas4.content,datas4.create_data,datas4.icon]></more-donor>
                    </div>
                    <div class="d-flex justify-content-end" style="margin-top:10px;">
                      <button @click="donor" type="button" class="btn btn-primary btn-sm">加载更多</button>
                    </div>
                  </div>
                  <div class="tab-pane fade" id="list-messages" role="tabpanel" aria-labelledby="list-messages-list">
                    3
                  </div>
                  <div class="tab-pane fade" id="list-settings" role="tabpanel" aria-labelledby="list-settings-list">
                    <more-course/>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <!-- 右边 -->
        <div class="col-md-3">
          <div class="diyrightset shadow p-3 bg-body rounded">
            <div class="diylefttop">
              <div class="diylefttop border-bottom">
                分栏
              </div>
            </div>
            <div class="diymidinsidebottom">
              <div>
                <div class="list-group" id="list-tab" role="tablist">
                  <a class="list-group-item list-group-item-action active" id="list-home-list" data-bs-toggle="list" href="#list-home" role="tab" aria-controls="list-home">主要</a>
                  <a  @click="donor" class="list-group-item list-group-item-action" id="list-profile-list" data-bs-toggle="list" href="#list-profile" role="tab" aria-controls="list-profile">受限</a>
                  <a class="list-group-item list-group-item-action disabled" id="list-messages-list" data-bs-toggle="list" href="#list-messages" role="tab" aria-controls="list-messages">其他</a>
                  <a class="list-group-item list-group-item-action" id="list-settings-list" data-bs-toggle="list" href="#list-settings" role="tab" aria-controls="list-settings">下载教程</a>
                </div>
              </div>
                <hr>
            </div>
          </div>
        </div>
        <div class="row">
            <div class="col-md-12 d-flex justify-content-center">
                <small style="font-size:10px">Copyright &copy; 2021 OOPS</small>
            </div>
        </div>
    </div>
  </div>

  

  <div>

  </div>
        
    </div>
</template>





<script>
import '@/assets/css/more.css'
import MoreChoice from '@/components/more/more_choice.vue'
import MoreDonor from '@/components/more/more_donor.vue'
import MoreCourse from '@/components/more/more_course.vue'


export default {
  name: 'More',
  components: {
      MoreChoice,
      MoreDonor,
      MoreCourse,
  },
  data(){
        return{
          "pagenum1":Number,
          "pagenum2":Number,
          "pagenum3":Number,
          "max_page":'123',
          'x':0,
          'x_count':Number,
          // 这里必须和后端传入的数据格式一模一样
          data:{
          "count": Number,
          "next": "",
          "previous": '',
          "results":
                    [{
                    id:"",
                    name:"",
                    introduce:"",
                    size: "",
                    version: "",
                    content: "",
                    link: "",
                    create_data: "",
                    isshow: '',
                    }],
          },
          data2:{
          "count": Number,
          "next": "",
          "previous": '',
          "results":
                    [{
                    id:"",
                    name:"",
                    introduce:"",
                    size: "",
                    version: "",
                    content: "",
                    create_data: "",
                    icon:'',
                    }],
          },
        }
  },
  mounted(){
    // -------------------------------------------
    // 获取id
    var params1 = this.$route.params;
    var link = JSON.stringify(params1);
    var zz = /["{id:}"]/g;
    this.pagenum2 = link.replace(zz,"");
    this.pagenum1 = this.pagenum2-1;
    this.pagenum3 = this.pagenum1+2;
    let __this = this; //定义一个变量
    let pagenum = this.pagenum2;
    this.$axios.get(`http://81.68.105.198:8002/api/more/?page=${pagenum}`)
    .then(function (response){ //response接收数据对象
      __this.data= response.data; //把接收到的数据对象传入data中
      __this.max_page = Math.ceil(__this.data.count.toString()/10); //把数据转成字符串并除以每页的内容得到总页数
      console.log(__this.data2.icon)
      })
    .catch(function (error){
      console.log(error);
    });
    // -------------------------------------------
  },
  methods:{
    // -------------------------------------------------
    gotopage1:function(){
      if (this.pagenum1 == 0)
      {
        alert("前面已经没有了")
      }
      else
      {
        window.location.href=`http://81.68.105.198:70/#/more/${this.pagenum1}`;
        this.$router.go(0);
      }
    },
    gotopage2:function(){
      if (this.pagenum2 == 0)
      {
        alert("前面已经没有了")
      }
      else if (this.pagenum3 >= this.max_page)
      {
        this.isdisabled = true;
      }
      else
      {
        window.location.href=`http://81.68.105.198:70/#/more/${this.pagenum2}`;
        this.$router.go(0);
      }
    },
    gotopage3:function(){
      if (this.pagenum3 == 0)
      {
        alert("前面已经没有了")
      }
      else if (this.pagenum3 > this.max_page)
      {
        alert("已经是最后一页了")
      }
      else
      {
        // window.open(`http://172.20.10.4:8080/#/more/${this.pagenum3}`)
        window.location.href=`http://81.68.105.198:70/#/more/${this.pagenum3}`;
        this.$router.go(0);
      }
    },
    // -----------------------------------------------------
    donor:function(){
      let __this = this;
      if ( __this.x/2 >= Math.ceil(__this.data2.count/2))
      {
        alert('没有更多了');
      }
      else
      {
        __this.x+=2;
        this.$axios.get(`http://81.68.105.198:8002/api/Donor/?page=1&size=${__this.x}`)
        .then(function (response){
          __this.data2 = response.data;
        })
        .catch(function (error){
          console.log(error);
        });
      }
    }
    // -----------------------------------------------------

  },
}
</script>