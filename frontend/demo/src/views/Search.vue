<template>
    <div class="about" style="margin-top:90px;">
        <div class="container">
            <div class="row">
                <div class="col-md-8 offset-md-2">
                    <span class="fs-4">根据关键字</span>
                    <span class="fs-4" style="color:blue">“{{ this.num }}”</span>
                    <span class="fs-4">搜索到</span>
                    <span class="fs-4" style="color:blue">{{ this.count }}</span>
                    <span class="fs-4">个资源</span>
                    <div class="fw-light">Tips:只有非受限资源才能被搜索显示出来</div>
                </div>
                <div class="col-md-8 offset-md-2">
                    <div v-for="data in searchdata">
                        <demo-mains :send=[data.pk,data.fields.name,data.fields.introduce,data.fields.version,data.fields.create_data]></demo-mains>
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
import DemoMains from '@/components/demo_mains.vue'


export default {
    name:'Search',
    components: {
        DemoMains
    },
    data(){
        return{
            searchdata:{
                "model": "",
                "pk": Number,
                "fields": {
                    "name": "",
                    "introduce": "",
                    "size": "",
                    "version": "",
                    "content": "",
                    "link": "",
                    "create_data": "",
                    "isshow": "",
                    "code": ""
                },
            },
            num:'',
            count:0,
        }
    },
    mounted(){
        // 获取id
        var params1 = this.$route.params;
        var link = JSON.stringify(params1);
        var zz = /["{iS:}"]/g;
        this.num = link.replace(zz,"");
        console.log(this.num)

        let __this = this;
        let data = {"search":__this.num};
        this.$axios.post('http://81.68.105.198:8002/api/v1/SearchView/',data)
        .then(function(response){
            __this.searchdata = response.data;
            __this.count = response.data.length;
        })
        .catch(function (error){
                console.log(error);
        });
    }
}
</script>