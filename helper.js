const fs = require('fs');

module.exports = {
    getPittsburghRestaurantsData : function (callback) {
        fs.readFile('attributes_pitt_restaurants.dat', 'utf8', function (err, data) {
            if (err) {
                return callback({message: 'Cannot get the local Pittsburgh restaurants data', data: null});
            }
            var rows = data.split('\n');
            var dic = {};
            for (var i = 0; i < rows.length; i++) {
                words = rows[i].split('\t');
                if (words.length != 12) {
                    continue;
                }
                dic[words[0]] = {};
                temp_dic = dic[words[0]];
                temp_dic['Alcohol'] = words[1];
                temp_dic['Ambience'] = {};
                var words_ambience = words[2].split(' ');
                for (var j = 0; j < words_ambience.length; j++) {
                    temp_dic['Ambience'][words_ambience[j]] = 1;
                }
                temp_dic['Dietary'] = {};
                var words_dietary = words[3].split(' ');
                for (var j = 0; j < words_dietary.length; j++) {
                    temp_dic['Dietary'][words_dietary[j]] = 1;
                }
                temp_dic['Parking'] = {};
                var words_parking = words[4].split(' ');
                for (var j = 0; j < words_parking.length; j++) {
                    temp_dic['Parking'][words_parking[j]] = 1;
                }
                temp_dic['Music'] = {};
                var words_music = words[5].split(' ');
                for (var j = 0; j < words_music.length; j++) {
                    temp_dic['Music'][words_music[j]] = 1;
                }
                temp_dic['NoiseLevel'] = words[6];
                temp_dic['PriceRange'] = words[7];
                temp_dic['Attire'] = words[8];
                temp_dic['GoodForMeal'] = {};
                var words_goodForMeal = words[9].split(' ');
                for (var j = 0; j < words_goodForMeal.length; j++) {
                    temp_dic['GoodForMeal'][words_goodForMeal[j]] = 1;
                }
                temp_dic['BestNight'] = {};
                var words_BestNight = words[10].split(' ');
                for (var j = 0; j < words_BestNight.length; j++) {
                    temp_dic['BestNight'][words_BestNight[j]] = 1;
                }
                temp_dic['Others'] = {};
                var words_others = words[11].split(' ');
                for (var j = 0; j < words_others.length; j++) {
                    temp_dic['Others'][words_others[j]] = 1;
                }
            }
            return callback({message: 'SUCCESS', data: dic});
        });
    },


    getPittsburghRestaurantsReviews : function (callback) {
        fs.readFile('pitt_restaurants_review_compressed.dat', 'utf8', function (err, data) {
            if (err) {
                return callback({message: 'Cannot get the local Pittsburgh restaurants review data', data: null});
            }
            var rows = data.split('\n');
            var dic = {};
            for (var i = 0; i < rows.length; i++) {
                var items = rows[i].split('\t');
                var key = items[0] + '\t' + items[1];
                if (items[0].length == 0 || items[1].length == 0) {
                    continue;
                }
                dic[key] = {};
                var total_word_count = 0;
                for (var j = 2; j < items.length; j++) {
                    var word = items[j].split(':')[0];
                    var freq = parseInt(items[j].split(':')[1]);
                    total_word_count += freq;
                    dic[key][word] = freq;
                }
                dic[key]['total_word_count'] = total_word_count;
            }
            return callback({message: 'SUCCESS', data: dic});
        });
    }
}
