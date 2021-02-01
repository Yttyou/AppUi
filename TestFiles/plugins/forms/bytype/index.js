var BytypeFormModel = Backbone.Collection.extend({
    url: 'data/bytype.json'
})

class Bytype extends allure.components.AppLayout {

    initialize() {
        this.model = new BytypeFormModel();
    }

    loadData() {
        return this.model.fetch();
    }

    getContentView() {
        return new BytypeView({ items: this.model.models });
    }
}

const bytype_template = function (data) {
    html = `<div class="pane__title pane__title_borderless"><span class="pane__title-text">分类统计</span></div>`
    html += `<div style="overflow-y: scroll;height: 100vh;">
            <table class="attachment__table" id="form"><thead><tr>
            <th>类型</th>
            <th>数量</th>
            <th>总数</th>
            <th>比率</th>
            </tr></thead>`;
    html += `<tbody>`;
    for (var item of data.items) {
        html += `<tr>
                <td>${item.attributes['Type']}</td>
                <td>${item.attributes['QTY']}</td>
                <td>${item.attributes['Total']}</td>
                <td>${(item.attributes['Rate'] * 100).toFixed(2)}%</td>
                </tr>`;
    }
    html += `</tbody></table></div>`;
    return html;
}
//在allure报告的左边增加一个tab按钮
var BytypeView = Backbone.Marionette.View.extend({
    template: bytype_template,

    render: function () {
        this.$el.html(this.template(this.options));
        return this;
    }
})

//
allure.api.addTab('bytype', {
    title: 'tab.bytype.name', icon: 'fa fa-table',
    route: 'bytype',
    onEnter: (function () {
        return new Bytype()
    })
});

// wiget中展示
class BytypeWidget extends Backbone.Marionette.View {

    template(data) {
        return widgetTemplate(data)
    }

    serializeData() {
        return {
            items: this.model.get('items'),
        }
    }
}

allure.api.addWidget('bytype_widget', BytypeWidget);

// 多语言支持。使用位置：allure.api.addTab() 中的 title 项
allure.api.addTranslation('zh', {
    tab: {
        bytype: {
            name: '分类统计'
        }
    }
});

allure.api.addTranslation('zt', {
    tab: {
        bytype: {
            name: '分類統計'
        }
    }
});

allure.api.addTranslation('en', {
    tab: {
        bytype: {
            name: 'By Status'
        }
    }
});