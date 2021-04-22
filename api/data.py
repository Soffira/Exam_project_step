import cherrypy

userss = {
    '1': {
        'username': 'van',
        'email': 'vanbyvan@fmail.ru',
        'department': 'production',
        'date_joined': '2011-11-11T11:10:09' 
    },
    '2': {
        'username': 'billy',
        'email ': 'billyjeans@fmail.ru',
        'department': 'pr',
        'date_joined': '1983-03-02T12:12:53'
    },
    '3': {
        'username': 'max',
        'email ': 'maximus@fmail.ru',
        'department': 'production',
        'date_joined': '1999-05-29T14:14:28'
    },
    '4': {
        'username': 'leonard',
        'email ': 'leokapri@fmail.ru',
        'department': 'sales',
        'date_joined': '1974-12-11T14:45:32'
    }
}

class Users:
    def GET(self, username=None, department=None):
        inf1 = []
        inf2 = []
        if username == None:
            for user in userss:
                inf1.append(userss[user])
        else:
            for user in userss:
                if username in userss[user]['username']:
                    inf1.append(userss[user])
        if department == None:
            for dep in userss:
                inf2.append(userss[dep])
        else:
            for dep in userss:
                if department in userss[dep]['department']:
                    inf2.append(userss[dep])
        inf3 = []
        for i in inf1:
            if i in inf2:
                inf3.append(i)
        return ('data: %s' % inf3)

        if username == None and department == None:
            return ("Error: No id field provided. Please specify information")
    
    exposed = True
# api.add_resource(Users, '/users')

class Departments:
    def GET(self, department=None):
        deps1 = []
        if department == None:
            for dep in userss:
                deps1.append(userss[dep]["department"])
            return ('Departments: %s' % list(set(deps1)))
        else:
            for dep in userss:
                if department in userss[dep]['department']:
                    deps1.append(userss[dep])       
        return ('data: %s' % deps1)
    exposed = True

if __name__ == '__main__':
# def serv_start():
    cherrypy.tree.mount(
        Users(), '/api/users', {
            '/': 
                {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
        }
    )
    cherrypy.tree.mount(
        Departments(), '/api/department',
        {'/':
            {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
        }
    )
    # import cherrypy
    cherrypy.config.update({'server.socket_host': '0.0.0.0', 'server.socket_port': 8080})
    cherrypy.engine.start()
    cherrypy.engine.block()

    cherrypy.quickstart()
