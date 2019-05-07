$(document).ready(function(){
                $("[data-toggle='popover']").popover();
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
                $("#del_note").on('click',function(){
                    var url = '/delete_cgi';
                    // 执行删除操作
                    $('#del_note').attr("data-dismiss","modal");
                });
                $('#modal-container-523565').on('hide.bs.modal', function () {
                  // 执行一些动作...
                  alert("保存成功！")
                });
            });