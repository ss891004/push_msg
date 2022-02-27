from models.wx_user import WxUser

# 员工号和企业微信账号有对应关系
def get_qywx_user_id(hrcb_user):

    emp_data=(hrcb_user).split('|')

    print(emp_data)
    new_emp_data=[]
    for i in emp_data:
        wx_id=WxUser.query.filter_by(emp_no=i).first()
        if wx_id is not None:
            new_emp_data.append(wx_id.wx_user_id)
            new_emp_data.append('|')

    return ''.join(new_emp_data[:-1])