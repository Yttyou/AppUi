// 读取覆盖率 json
var model2JSON;
var url = "data/rate_data.json";
var request = new XMLHttpRequest();
request.open("get", url);
request.send(null);
request.onload = function () {
    model2JSON = JSON.parse(request.responseText);
}

var SP_BP_resultsFormModel = Backbone.Collection.extend({
    url: 'data/SP_BP_results.json'
})

class Covered extends allure.components.AppLayout {

    initialize() {
        this.model = new SP_BP_resultsFormModel();
    }

    loadData() {
        return this.model.fetch();
    }

    getContentView() {
        return new CoveredView({ items: this.model.models, items2: model2JSON});
    }
}

const covered_template = function (data) {
    // 覆盖率 html
    html = `<div class="pane__title pane__title_borderless"><span class="pane__title-text">覆盖率</span></div>`
    html += `<div style="overflow-y: scroll;max-height: 50vh;">
            <table class="attachment__table" id="form"><thead><tr>
            <th>模块</th>
            <th>覆盖率</th>
            </tr></thead>`;    
    html += `<tbody>`;
    for (var item2 of data.items2) {
        html += `<tr>
                <td>${item2['Module']}</td>
                <td>${(item2['Coverage Rate'] * 100).toFixed(2)}%</td>`
    }
    html += `</tbody></table></div>`;
    // 覆盖模块 html
    html += `<div class="pane__title pane__title_borderless" style="margin-top: 20px"><span class="pane__title-text">覆盖模块</span></div>`
    html += `<div style="overflow-y: scroll;height: 100vh;">
            <table class="attachment__table" id="form"><thead><tr>
            <th>一级模块</th>
            <th>二级模块</th>
            <th>三级模块</th>
            <th>四级模块</th>
            <th>五级模块</th>
            <th>功能是否覆盖</th>
            </tr></thead>`;
    html += `<tbody>`;
    for (var item of data.items) {
        html += `<tr>
                <td>${item.attributes['1']}</td>
                <td>${item.attributes['2']}</td>
                <td>${item.attributes['3']}</td>
                <td>${item.attributes['4']}</td>
                <td>${item.attributes['5']}</td>
                <td>${item.attributes['Covered']}</td>
                </tr>`;
    }
    html += `</tbody></table></div>`;
    return html;
}
//在allure报告的左边增加一个tab按钮
var CoveredView = Backbone.Marionette.View.extend({
    template: covered_template,

    render: function () {
        this.$el.html(this.template(this.options));
        return this;
    }
})

//
allure.api.addTab('covered', {
    title: 'tab.covered.name', icon: 'fa fa-table',
    route: 'covered',
    onEnter: (function () {
        return new Covered()
    })
});

// wiget中展示
class CoveredWidget extends Backbone.Marionette.View {

    template(data) {
        return widgetTemplate(data)
    }

    serializeData() {
        return {
            items: this.model.get('items'),
        }
    }
}

allure.api.addWidget('covered_widget', CoveredWidget);

// 多语言支持。使用位置：allure.api.addTab() 中的 title 项
allure.api.addTranslation('zh', {
    tab: {
        covered: {
            name: '覆盖率'
        }
    }
});
allure.api.addTranslation('zt', {
    tab: {
        covered: {
            name: '覆蓋率'
        }
    }
});

allure.api.addTranslation('en', {
    tab: {
        covered: {
            name: 'Coverage Rate'
        }
    }
});