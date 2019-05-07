$(document).ready(function(){
                $("[data-toggle='popover']").popover();
                //退出登录
                $("#logout").on('click',function(){
                    var url = '/logout_cgi';
                    $.post(url,function(json){
                        if(json.ret == 0){
                            window.location.href = "/login";
                        }else{
                            alert("退出失败，请重试！")
                        }
                    },'json')
                });
                //删除笔记js
                $("#del_note").on('click',function(){
                    var url = '/delete_cgi';
                    // 执行删除操作
                    $('#del_note').attr("data-dismiss","modal");
                    alert("删除成功！")
                });
                //保存笔记js
                $('#modal-container-523565').on('hide.bs.modal', function(){
                  // 执行一些动作...
                  alert("保存成功！")
                });
                // 添加笔记按钮js
                $("#add_note").on('click',function(){
                    var url = '/add_cgi';
                });
            });