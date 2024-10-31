



data_file_path = {
    '/result_DDr.txt', ...
    '/result_FedCS.txt', ...
    '/result_RandCS.txt'
};

y_label = {
    'Số máy khách tham gia huấn luyện', ...
    'Tổng lượng data tham gia huấn luyện', ...
    'Mất mát', ...
    'Độ chính xác'
};

y_limit = {
    150, ...
    5000, ...
    2.5, ...
    1
};

examined_factor = {
    'clients_num', ...
    'data_used', ...
    'loss', ...
    'accuracy'
};

markerIndices = 1:1:10; % Adjust the step to control marker frequency

datapath = '/Users/thanhdaonguyen/Documents/Thành Đạo/11. Cloud Computing/5. projects/Dao+Thien_PTIT project/Client_Selection_in_FL/results';

for i = 1:4
    
    figure('Position', [floor( (i - 1) / 2) * 650, mod( (i - 1) , 2) * 450, 550, 350]); % Adjust the position and size as needed
    % Read data from the TSV files
    dataFedCS = readmatrix([datapath, '/result_FedCS.txt']);
    dataDDrCS = readmatrix([datapath, '/result_DDrCS.txt']);

    % Plot queueing times
    hold on;
    plot(dataFedCS(:, 1), dataFedCS(:, i + 1), '->', 'DisplayName', 'FedCS', 'Color', 'blue', 'LineWidth', 1.3, 'MarkerIndices', markerIndices, 'MarkerSize', 5);
    plot(dataDDrCS(:, 1), dataDDrCS(:, i + 1), '-o', 'DisplayName', 'DDrCS', 'Color', 'red', 'LineWidth', 1.3, 'MarkerIndices', markerIndices, 'MarkerSize', 5);
 
    ylim([0, y_limit{i}]);
    xlabel('Vòng huấn luyện', 'FontSize', 17);
    xticks(1:1:10);
    ylabel(y_label{i}, 'FontSize', 17);
    % title(['Efficiency over range of ', changing_factor{i}], 'FontSize', 15);
    hold off;
    grid on
    legend('show', 'FontSize', 14);
    set(gca, 'FontSize', 14);

end

% Show the plots
% tightfig;  % Adjust the figure layout to remove excess white space
