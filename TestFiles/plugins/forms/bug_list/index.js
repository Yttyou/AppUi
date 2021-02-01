var BugListFormModel = Backbone.Collection.extend({
    url: 'data/bug_list.json'
})

class BugList extends allure.components.AppLayout {

    initialize() {
        this.model = new BugListFormModel();
    }

    loadData() {
        return this.model.fetch();
    }

    getContentView() {
        return new BugListView({ items: this.model.models });
    }
}

const bug_list_template = function (data) {
    html = `<div class="pane__title pane__title_borderless"><span class="pane__title-text">BUG 列表</span></div>`
    html += `<div style="overflow-y: scroll;height: 100vh;">
            <table class="attachment__table" id="form"><thead><tr>
            <th>标题</th>
            <th>严重程度</th>
            <th>模块</th>
            <th>日期</th>
            </tr></thead>`;
    html += `<tbody>`;
    for (var item of data.items) {
        html += `<tr>
                <td><a href="${item.attributes['Defect Link']}">${item.attributes['Title']}</a></td>
                <td>${item.attributes['Severity']}</td>
                <td>${item.attributes['Module']}</td>
                <td>${item.attributes['DateTime']}</td>
                </tr>`;
    }
    html += `</tbody></table></div>`;
    return html;
}
//在allure报告的左边增加一个tab按钮
var BugListView = Backbone.Marionette.View.extend({
    template: bug_list_template,

    render: function () {
        this.$el.html(this.template(this.options));
        return this;
    }
})

//
allure.api.addTab('bug_list', {
    title: 'tab.bug_list.name', icon: 'fa fa-table',
    route: 'bug_list',
    onEnter: (function () {
        return new BugList()
    })
});

// wiget中展示
class BugListWidget extends Backbone.Marionette.View {

    template(data) {
        return widgetTemplate(data)
    }

    serializeData() {
        return {
            items: this.model.get('items'),
        }
    }
}

allure.api.addWidget('bug_list_widget', BugListWidget);

// 多语言支持。使用位置：allure.api.addTab() 中的 title 项
allure.api.addTranslation('zh', {
    tab: {
        bug_list: {
            name: 'Defect 列表'
        }
    }
});
allure.api.addTranslation('zt', {
    tab: {
        bug_list: {
            name: 'Defect 列表'
        }
    }
});
allure.api.addTranslation('en', {
    tab: {
        bug_list: {
            name: 'Defect List'
        }
    }
});