<template>
    <div class="news" style="margin-top:90px;">
        <div class="container">
            <div class="row">
                <div class="col-md-8 offset-md-2">
                    <div class="shadow p-3 mb-5 bg-body rounded">
                        <div>
                            <img src="@/assets/OOPS.png" style="height:30px;" alt="">
                                <hr>
                                <div>
                                    <strong>{{ data.name }}</strong>
                                </div>
                                <div style="color:#6C757D">
                                    {{ data.content }}
                                </div>
                                <hr>
                                用户:{{ data.auth }} 编辑于:{{ data.create_data }}
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
    </div>
</template>



<script>
export default {
    name:"News",
    data(){
        return{
            data:{
              id:"",
              name:"",
              content:"",
              auth:"",
              create_data:"",
            },
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
        this.$axios.get(`http://81.68.105.198:8002/api/News/${nums}`)
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