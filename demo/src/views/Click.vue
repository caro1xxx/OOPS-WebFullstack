<template>
    <div>
        <div class="container diybodyset">
            <div class="row">
                <div class="col-md-9">
                    <div>
                        <div>
                            <div class="border-bottom shadow p-3 bg-body rounded">
                                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-download" viewBox="0 0 16 16">
                                    <path d="M.5 9.9a.5.5 0 0 1 .5.5v2.5a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1v-2.5a.5.5 0 0 1 1 0v2.5a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2v-2.5a.5.5 0 0 1 .5-.5z"/>
                                    <path d="M7.646 11.854a.5.5 0 0 0 .708 0l3-3a.5.5 0 0 0-.708-.708L8.5 10.293V1.5a.5.5 0 0 0-1 0v8.793L5.354 8.146a.5.5 0 1 0-.708.708l3 3z"/>
                                </svg>
                                下载
                            </div>
                            <div class="row">
                                <div class="col-12" style="padding:10px;">
                                    <div class="tab-content" id="nav-tabContent">
                                        <div class="tab-pane fade show active" id="list-home" role="tabpanel" aria-labelledby="list-home-list">
                                            <div class="row">
                                                <div class="col-md-12">
                                                    <click-body :send=[data.id,data.name,data.introduce,data.size,data.version,data.content,data.link,data.create_data,data.isshow,data.code]></click-body>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="tab-pane fade" id="list-profile" role="tabpanel" aria-labelledby="list-profile-list">
                                            <div class="row">
                                                <div class="col-md-12">
                                                    <click-course/>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="tab-pane fade" id="list-messages" role="tabpanel" aria-labelledby="list-messages-list">3</div>
                                        <div class="tab-pane fade" id="list-settings" role="tabpanel" aria-labelledby="list-settings-list">4.</div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>  
                </div>
                <div class="col-md-3" style="float:right;">
                    <div class="shadow p-3 bg-body rounded">
                        <div class="diylefttop">
                            <div class="diylefttop border-bottom">
                                分栏
                            </div>
                        </div>
                        <div>
                            <div class="col-12" style="margin-top:10px;">
                                <div class="list-group" id="list-tab" role="tablist">
                                    <a class="list-group-item list-group-item-action active" id="list-home-list" data-bs-toggle="list" href="#list-home" role="tab" aria-controls="list-home">主要的</a>
                                    <a class="list-group-item list-group-item-action" id="list-profile-list" data-bs-toggle="list" href="#list-profile" role="tab" aria-controls="list-profile">下载教程</a>
                                    <a class="list-group-item list-group-item-action disabled" id="list-messages-list" data-bs-toggle="list" href="#list-messages" role="tab" aria-controls="list-messages">反馈</a>
                                </div>
                            </div>
                                <hr>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>     
</template>





<script>
import '@/assets/css/click.css'
import ClickBody from '@/components/click/click_body.vue'
import ClickCourse from '@/components/click/click_course.vue'



export default {
  name: 'Click',
  components: {
      ClickBody,
      ClickCourse,
  },
  data(){
        return{
            // 这里必须和后端传入的数据格式一模一样
            data:{
                id:"",
                name:"",
                introduce:"",
                size: "",
                version: "",
                content: "",
                link: "",
                create_data: "",
                isshow: '',
                code:'',
            },
            num:'',
        }
    },
    mounted(){
        // 获取id
       var params1 = this.$route.params;
        var link = JSON.stringify(params1);
        var zz = /["{id:}"]/g;
        this.num = link.replace(zz,""); 

        // 请求数据
        var nums = this.num;
        var __this = this; //定义一个变量
        this.$axios.get(`http://81.68.105.198:8002/api/more/${nums}`)
        .then(function (response){ //response接收数据对象
        __this.data= response.data; //把接收到的数据对象传入data中
        console.log(__this.data)
        })
        .catch(function (error){
        console.log(error);
        });
    }
}
</script>