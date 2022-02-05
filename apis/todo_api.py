
from flask_restx import Namespace,fields,Resource
from  .model import TodoDao

ns = Namespace('Todo_API', description='Todo_API')

model = ns.model('Model', {
    'task': fields.String,
    'xxx': fields.String,
    'yyyy':fields.String,
    #'uri': fields.Url('todo_ep')
})



@ns.route('/aaaa')
class Todo(Resource):
    @ns.marshal_with(model)
    def get(self, **kwargs):
        return TodoDao(todo_id='my_todo', task='Remember the milk')