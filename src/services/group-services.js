app.factory('groupServices', ['$http', '$log',
  function($http, $log) {

    function get(url) {
      return processAjaxPromise($http.get(url));
    }
    function post(url, share) {
      return processAjaxPromise($http.post(url, share));
    }
    function put(url, share) {
      return processAjaxPromise($http.put(url, share));
    }
    function remove(url) {
      return processAjaxPromise($http.delete(url));
    }
    function processAjaxPromise(p) {
      return p.then(function(result) {
        return result.data.data;
      })
      .catch(function(error) {
        $log.log(error);
      });
    }

    return {

      list: function () {
        return get('/api/v1/groups');
      },

      getByGroupId: function (groupId) {
        return get('/api/v1/groups/' + groupId);
      },

      listGroups: function () {
        return get('/api/v1/groups')
      },

      listCats: function () {
        return get('/api/v1/categories')
      }

    };
  }
]);